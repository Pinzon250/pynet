"""
Subpaquete admin: CLI separado para tareas administrativas.

Entry point: `pynet-admin` (declarado en pyproject.toml).

Comandos:
- pynet-admin client add/list/show/remove   → gestionar clientes
- pynet-admin token issue/list/revoke       → emitir/auditar tokens

Este módulo NO se usa desde el CLI dev (`pynet`). Lo invocan solo los
administradores autorizados (que tienen credenciales de gestión del
backend, distintas al token de un solo uso del dev).
"""
