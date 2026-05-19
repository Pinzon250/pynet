"""
pynet.core.auth
---------------
Resolución del token de acceso del dev.

En el modelo de tokens de un solo uso, NO hay login persistente.
El token llega por dos fuentes (en orden de precedencia):

    1. Flag --token <X>      (mayor prioridad — uso explícito puntual)
    2. PYNET_TOKEN env var   (uso en CI/CD, contenedores)

Si en el futuro se introducen tokens de larga duración (ej. para CI con
service accounts), se podría agregar una tercera fuente: archivo de config
local. Por ahora se deja fuera para mantener el modelo simple.
"""

import os
from typing import Optional

from pynet.utils.exceptions import TokenNotProvidedError


ENV_VAR = "PYNET_TOKEN"


def resolve_token(cli_flag: Optional[str] = None) -> str:
    """
    Resuelve el token activo según orden de precedencia.

    Args:
        cli_flag: Valor del flag --token si se pasó al comando, None si no.

    Returns:
        El token resuelto (string).

    Raises:
        TokenNotProvidedError: Si no hay token en ninguna fuente.
    """
    # 1. Flag explícito
    if cli_flag:
        return cli_flag.strip()

    # 2. Variable de entorno
    env_value = os.getenv(ENV_VAR, "").strip()
    if env_value:
        return env_value

    # No hay token
    raise TokenNotProvidedError(
        f"No se encontró un token de acceso.\n"
        f"  • Pasa --token <TOKEN> al comando, o\n"
        f"  • Exporta {ENV_VAR}=<TOKEN> antes de ejecutarlo.\n"
        f"Si no tienes un token, solicítalo a un administrador."
    )


def token_source(cli_flag: Optional[str] = None) -> str:
    """
    Devuelve el nombre de la fuente del token (para mostrar al usuario).
    Útil para mensajes tipo "usando token de la variable PYNET_TOKEN".

    Returns:
        "flag" | "env" | "none"
    """
    if cli_flag:
        return "flag"
    if os.getenv(ENV_VAR, "").strip():
        return "env"
    return "none"
