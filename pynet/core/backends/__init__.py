"""
pynet.core.backends
-------------------
Backends de credenciales. Expone:
  - La interfaz abstracta CredentialsBackend (base.py)
  - Implementaciones concretas (azure_kv.py, ...)
  - Una factory `get_backend()` para obtener la instancia configurada.
"""

from pynet.core.backends.base import (
    CredentialsBackend,
    AuthContext,
    ClientCredentials,
)


def get_backend(backend_type: str = "azure_kv") -> CredentialsBackend:
    """
    Factory: devuelve la instancia del backend solicitado.

    Args:
        backend_type: Identificador del backend.
            Soportados (futuros):
              - "azure_kv": Azure Key Vault corporativo (default)
              - "rest_api": API REST propia (no implementado)

    Returns:
        Instancia de CredentialsBackend lista para usar.
    """
    if backend_type == "azure_kv":
        # Import diferido: solo se carga si se pide este backend
        # (evita exigir azure-identity cuando no se usa).
        from pynet.core.backends.azure_kv import AzureKeyVaultBackend
        return AzureKeyVaultBackend()

    raise ValueError(
        f"Backend '{backend_type}' no soportado. "
        f"Opciones: 'azure_kv'."
    )


__all__ = [
    "CredentialsBackend",
    "AuthContext",
    "ClientCredentials",
    "get_backend",
]
