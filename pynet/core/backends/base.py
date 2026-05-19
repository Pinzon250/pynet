"""
pynet.core.backends.base
------------------------
Interfaz abstracta para los backends de credenciales.

Un backend es cualquier sistema capaz de:
  1. Recibir un token de un solo uso.
  2. Validar el token (existe, no consumido, no expirado).
  3. Consumirlo (marcarlo como usado de forma atómica).
  4. Devolver las credenciales de conexión al Azure KV del cliente
     que ese token autoriza.

Las implementaciones concretas (Azure KV corporativo, API REST propia, etc.)
viven en otros módulos del paquete `backends/` y heredan de aquí.

Esta abstracción permite cambiar el backend sin tocar el CLI.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ── Dataclasses de respuesta ──────────────────────────────────────────────

@dataclass
class ClientCredentials:
    """
    Credenciales de conexión al Azure Key Vault de UN cliente.

    Esto es lo que el backend devuelve al consumir un token.
    Son los 4 valores que el bot necesita para luego descargar
    los secretos REALES (SAP, DB, portales) del KV del cliente.
    """
    vault_url: str       # https://<cliente>.vault.azure.net/
    tenant_id: str       # Azure AD Tenant ID
    client_id: str       # Service Principal Application ID
    client_secret: str   # Service Principal Secret (sensible)


@dataclass
class AuthContext:
    """
    Información sobre quién consumió el token y para qué.
    El CLI la usa para mensajes de auditoría y para validar
    que el cliente del token coincide con el del proyecto.
    """
    token_id: str               # ID corto del token (los primeros chars)
    client_slug: str            # Cliente autorizado por el token
    issued_to: Optional[str]    # Email/identificador del dev (si el backend lo guarda)
    consumed_at: datetime       # Cuándo se consumió
    metadata: dict = field(default_factory=dict)


# ── Interfaz abstracta ────────────────────────────────────────────────────

class CredentialsBackend(ABC):
    """
    Contrato que toda implementación de backend debe cumplir.

    Las implementaciones reales (AzureKeyVaultBackend, RestApiBackend, ...)
    heredan de aquí. El CLI siempre habla con esta interfaz, nunca con
    una implementación concreta directamente.
    """

    @abstractmethod
    def consume_token(self, token: str) -> tuple[AuthContext, ClientCredentials]:
        """
        Operación atómica: valida un token, lo marca como consumido,
        y devuelve las credenciales del cliente autorizado.

        Args:
            token: El token de un solo uso entregado por un admin.

        Returns:
            Tupla (contexto_de_auth, credenciales_del_cliente).

        Raises:
            TokenInvalidError: Token mal formado o desconocido.
            TokenAlreadyConsumedError: Token ya fue usado.
            TokenExpiredError: Token venció por TTL.
            BackendUnavailableError: No se pudo contactar al backend.
        """
        ...

    @abstractmethod
    def health_check(self) -> bool:
        """
        Verifica que el backend está disponible (sin consumir tokens).
        Útil para diagnóstico previo. Devuelve True si todo está OK.
        """
        ...
