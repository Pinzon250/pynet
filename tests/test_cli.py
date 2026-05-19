"""
Smoke tests del CLI del DEV.
Verifican que el CLI arranca, los comandos están registrados, y la
resolución de tokens funciona.
"""

import os
import pytest
from typer.testing import CliRunner

from pynet.cli.app import app
from pynet.__version__ import __version__


runner = CliRunner()


# ── Básicos ──────────────────────────────────────────────────────────────

def test_help_works():
    """`pynet --help` debe terminar con código 0."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "pynet" in result.stdout.lower()


def test_version_flag():
    """`pynet --version` debe imprimir la versión actual."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_no_args_shows_help():
    """`pynet` sin args muestra ayuda con los comandos disponibles."""
    result = runner.invoke(app, [])
    assert "create" in result.stdout
    assert "sync" in result.stdout


def test_client_command_removed():
    """`pynet client` ya no existe (se movió a pynet-admin)."""
    result = runner.invoke(app, ["client", "--help"])
    assert result.exit_code != 0


# ── Subcomando create ───────────────────────────────────────────────────

def test_create_help_works():
    """`pynet create --help` responde."""
    result = runner.invoke(app, ["create", "--help"])
    assert result.exit_code == 0


def test_create_app_requires_token():
    """Sin token (flag ni env), `pynet create app` falla con mensaje claro."""
    # Asegurar que no haya PYNET_TOKEN
    env = {k: v for k, v in os.environ.items() if k != "PYNET_TOKEN"}
    result = runner.invoke(app, ["create", "app", "MiBot"], env=env)
    assert result.exit_code == 1
    assert "token" in result.stdout.lower()


def test_create_app_with_token_flag():
    """Con --token, llega al placeholder de creación."""
    result = runner.invoke(
        app,
        ["create", "app", "MiBot", "--token", "pynet_ot_abc123"],
    )
    assert result.exit_code == 0
    assert "MiBot" in result.stdout


def test_create_app_with_env_var(monkeypatch):
    """Con PYNET_TOKEN en el entorno, llega al placeholder."""
    monkeypatch.setenv("PYNET_TOKEN", "pynet_ot_env_xyz")
    result = runner.invoke(app, ["create", "app", "OtroBot"])
    assert result.exit_code == 0
    assert "OtroBot" in result.stdout


# ── Subcomando sync ──────────────────────────────────────────────────────

def test_sync_command_exists():
    """`pynet sync --help` responde."""
    result = runner.invoke(app, ["sync", "--help"])
    assert result.exit_code == 0


def test_sync_requires_token():
    """Sin token, `pynet sync` falla con mensaje claro."""
    env = {k: v for k, v in os.environ.items() if k != "PYNET_TOKEN"}
    result = runner.invoke(app, ["sync"], env=env)
    assert result.exit_code == 1
    assert "token" in result.stdout.lower()


def test_sync_with_token_flag():
    """Con --token, llega al placeholder de sync."""
    result = runner.invoke(app, ["sync", "--token", "pynet_ot_def456"])
    assert result.exit_code == 0
    assert "sync" in result.stdout.lower()


# ── Precedencia: flag > env ──────────────────────────────────────────────

def test_flag_takes_precedence_over_env(monkeypatch):
    """Si hay flag Y env var, prevalece el flag."""
    monkeypatch.setenv("PYNET_TOKEN", "from_env_token_xyz")
    result = runner.invoke(
        app,
        ["create", "app", "TestBot", "--token", "from_flag_token_abc"],
    )
    assert result.exit_code == 0
    # El preview muestra los primeros 12 chars del token usado
    assert "from_flag_to" in result.stdout
