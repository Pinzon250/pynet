"""
pynet.core.backends.azure_kv
----------------------------
Implementación del backend usando un Azure Key Vault corporativo
de NetApplications como almacén de credenciales de clientes.

Modelo:
  - Hay UN Key Vault corporativo (no del cliente, de la empresa).
  - Por cada cliente, hay un secreto con su configuración:
        nombre:  client-{slug}-config
        valor:   JSON {vault_url, tenant_id, client_id, client_secret}
        tags:    {kind: "client_config"}
  - Por cada token emitido, hay un secreto:
        nombre:  token-{hash}
        valor:   JSON {client_slug, issued_to, status, exp, ...}
        tags:    {kind: "token"}
  - "Consumir" un token = actualizar su valor a status=consumed (atómico).

Esta implementación está pendiente. Por ahora levanta NotImplementedError
con un mensaje claro de qué falta hacer.
"""

from pynet.core.backends.base import (
    CredentialsBackend,
    AuthContext,
    ClientCredentials,
)


class AzureKeyVaultBackend(CredentialsBackend):
    """
    Backend basado en Azure Key Vault corporativo.

    Pendiente de implementación. Por ahora sirve como placeholder
    para mantener la arquitectura completa.
    """

    def __init__(self, vault_url: str = None):
        """
        Args:
            vault_url: URL del KV corporativo. Si None, se lee de
                       PYNET_CORPORATE_VAULT_URL (env var).
        """
        # TODO: leer config (vault_url corporativo, auth method)
        self.vault_url = vault_url

    def consume_token(self, token: str) -> tuple[AuthContext, ClientCredentials]:
        raise NotImplementedError(
            "AzureKeyVaultBackend.consume_token aún no está implementado.\n"
            "Pasos pendientes:\n"
            "  1. Conectar al KV corporativo (azure-identity).\n"
            "  2. Buscar el secreto 'token-{hash}' por nombre.\n"
            "  3. Validar status=unused y exp > now.\n"
            "  4. Actualizar a status=consumed (atómico).\n"
            "  5. Leer el secreto 'client-{slug}-config' del cliente vinculado.\n"
            "  6. Devolver (AuthContext, ClientCredentials)."
        )

    def health_check(self) -> bool:
        raise NotImplementedError(
            "AzureKeyVaultBackend.health_check aún no está implementado."
        )
