"""Tests unitarios de pynet.core.auth."""

import pytest

from pynet.core.auth import resolve_token, token_source, ENV_VAR
from pynet.utils.exceptions import TokenNotProvidedError


def test_resolve_from_flag():
    """El flag se usa directamente."""
    assert resolve_token("abc123") == "abc123"


def test_resolve_flag_is_trimmed():
    """Espacios en blanco al inicio/fin del flag se quitan."""
    assert resolve_token("  abc123  ") == "abc123"


def test_resolve_from_env(monkeypatch):
    """Sin flag, se lee la variable de entorno."""
    monkeypatch.setenv(ENV_VAR, "env_token")
    assert resolve_token(None) == "env_token"


def test_resolve_env_is_trimmed(monkeypatch):
    """Espacios en la env var también se quitan."""
    monkeypatch.setenv(ENV_VAR, "  env_token  ")
    assert resolve_token(None) == "env_token"


def test_flag_takes_precedence(monkeypatch):
    """Si hay flag y env var, prevalece el flag."""
    monkeypatch.setenv(ENV_VAR, "env_token")
    assert resolve_token("flag_token") == "flag_token"


def test_no_token_raises(monkeypatch):
    """Sin flag ni env, levanta TokenNotProvidedError."""
    monkeypatch.delenv(ENV_VAR, raising=False)
    with pytest.raises(TokenNotProvidedError):
        resolve_token(None)


def test_empty_string_is_not_a_token(monkeypatch):
    """Una env var vacía o solo espacios no cuenta como token."""
    monkeypatch.setenv(ENV_VAR, "   ")
    with pytest.raises(TokenNotProvidedError):
        resolve_token(None)


# ── token_source ─────────────────────────────────────────────────────────

def test_source_is_flag():
    assert token_source("abc") == "flag"


def test_source_is_env(monkeypatch):
    monkeypatch.setenv(ENV_VAR, "x")
    assert token_source(None) == "env"


def test_source_is_none(monkeypatch):
    monkeypatch.delenv(ENV_VAR, raising=False)
    assert token_source(None) == "none"
