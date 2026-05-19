"""Smoke tests del CLI admin (pynet-admin)."""

from typer.testing import CliRunner

from pynet.admin.app import app
from pynet.__version__ import __version__


runner = CliRunner()


def test_help_works():
    """`pynet-admin --help` responde."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "admin" in result.stdout.lower()


def test_version_flag():
    """`pynet-admin --version` imprime la versión."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_no_args_shows_help():
    """`pynet-admin` sin args muestra los comandos disponibles."""
    result = runner.invoke(app, [])
    assert "client" in result.stdout
    assert "token" in result.stdout


# ── Subcomando client ────────────────────────────────────────────────────

def test_client_help():
    result = runner.invoke(app, ["client", "--help"])
    assert result.exit_code == 0


def test_client_add_placeholder():
    result = runner.invoke(app, ["client", "add"])
    assert result.exit_code == 0


def test_client_list_placeholder():
    result = runner.invoke(app, ["client", "list"])
    assert result.exit_code == 0


def test_client_show_placeholder():
    result = runner.invoke(app, ["client", "show", "colsubsidio"])
    assert result.exit_code == 0


def test_client_remove_placeholder():
    result = runner.invoke(app, ["client", "remove", "colsubsidio"])
    assert result.exit_code == 0


# ── Subcomando token ─────────────────────────────────────────────────────

def test_token_help():
    result = runner.invoke(app, ["token", "--help"])
    assert result.exit_code == 0


def test_token_issue_placeholder():
    result = runner.invoke(
        app,
        ["token", "issue", "--client", "colsubsidio", "--for", "juan@empresa.com"],
    )
    assert result.exit_code == 0


def test_token_list_placeholder():
    result = runner.invoke(app, ["token", "list"])
    assert result.exit_code == 0


def test_token_revoke_placeholder():
    result = runner.invoke(app, ["token", "revoke", "abc123"])
    assert result.exit_code == 0
