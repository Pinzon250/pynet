"""
pynet.utils.exceptions
----------------------
Jerarquía de excepciones del framework.

Tener excepciones propias permite que el CLI las capture específicamente
y muestre mensajes claros, sin atrapar errores que no son de pynet.

Jerarquía:

    PynetError                          → base de todas
    ├── AuthError                       → problemas de autenticación
    │   ├── TokenNotProvidedError       → no se encontró token (flag/env)
    │   ├── TokenInvalidError           → token mal formado o desconocido
    │   ├── TokenAlreadyConsumedError   → token de un uso ya gastado
    │   └── TokenExpiredError           → token venció
    ├── BackendError                    → problemas con el backend de credenciales
    │   ├── BackendUnavailableError     → no se pudo conectar al backend
    │   └── ClientMismatchError         → el cliente del token no coincide con el del proyecto
    ├── TemplateError                   → problemas con plantillas Jinja2
    │   └── TemplateNotFoundError       → el template solicitado no existe
    ├── ProjectContextError             → problemas al construir el contexto del proyecto
    └── ManifestError                   → problemas con pynet.yaml
        ├── ManifestNotFoundError       → no hay pynet.yaml en el cwd
        └── ManifestInvalidError        → pynet.yaml mal formado o incompleto
"""


class PynetError(Exception):
    """Excepción base de pynet. Todas las demás heredan de aquí."""
    pass


# ── Autenticación (tokens) ────────────────────────────────────────────────

class AuthError(PynetError):
    """Errores relacionados con la autenticación por token."""
    pass


class TokenNotProvidedError(AuthError):
    """No se encontró un token en flag, variable de entorno ni config."""
    pass


class TokenInvalidError(AuthError):
    """El token está mal formado o no existe en el backend."""
    pass


class TokenAlreadyConsumedError(AuthError):
    """El token ya fue consumido (modelo de un solo uso)."""
    pass


class TokenExpiredError(AuthError):
    """El token venció por TTL."""
    pass


# ── Backend de credenciales ───────────────────────────────────────────────

class BackendError(PynetError):
    """Errores al interactuar con el backend de credenciales."""
    pass


class BackendUnavailableError(BackendError):
    """No se pudo conectar al backend (red, auth corporativa, etc.)."""
    pass


class ClientMismatchError(BackendError):
    """
    El cliente del token no coincide con el cliente del proyecto.

    Caso típico: el dev tiene un token para 'colsubsidio' pero el
    pynet.yaml del proyecto dice 'bbva'. Sería peligroso continuar.
    """
    pass


# ── Plantillas ────────────────────────────────────────────────────────────

class TemplateError(PynetError):
    """Errores en el sistema de plantillas."""
    pass


class TemplateNotFoundError(TemplateError):
    """El template solicitado no existe en el catálogo."""
    pass


# ── Contexto / Manifest del proyecto ──────────────────────────────────────

class ProjectContextError(PynetError):
    """Errores al construir o validar el ProjectContext."""
    pass


class ManifestError(PynetError):
    """Errores relacionados con el pynet.yaml de un proyecto."""
    pass


class ManifestNotFoundError(ManifestError):
    """No se encontró un pynet.yaml en el directorio actual."""
    pass


class ManifestInvalidError(ManifestError):
    """El pynet.yaml está mal formado o le faltan campos obligatorios."""
    pass
