"""
pynet.admin.commands.token
--------------------------
Subcomandos para emitir, listar y revocar tokens de un solo uso.

Modelo:
- Cada token autoriza UN proyecto/sync para UN cliente específico.
- Se consume al primer uso. Tras eso, queda como auditoría.
- Puede revocarse mientras siga en estado 'unused'.
"""

import typer
from rich.console import Console


token_app = typer.Typer(
    help="Emitir y administrar tokens de un solo uso.",
    no_args_is_help=True,
)
console = Console()


@token_app.command("issue")
def token_issue(
    client: str = typer.Option(
        ...,
        "--client", "-c",
        help="Slug del cliente para el que se emite el token.",
    ),
    issued_to: str = typer.Option(
        None,
        "--for",
        help="Email o identificador del dev que recibirá el token.",
    ),
    ttl_hours: int = typer.Option(
        72,
        "--ttl",
        help="Vida del token en horas si no se consume (default: 72).",
    ),
):
    """Emite un token de un solo uso vinculado a un cliente."""
    console.print(
        f"[yellow]⚠️  pynet-admin token issue: no implementado aún.[/yellow]\n"
        f"[dim]Cliente: {client} | Para: {issued_to or '(no especificado)'} | "
        f"TTL: {ttl_hours}h[/dim]\n"
        f"[dim]Se construirá en el paso 7 (CLI admin).[/dim]"
    )


@token_app.command("list")
def token_list(
    status: str = typer.Option(
        "all",
        "--status",
        help="Filtrar por estado: all | unused | consumed | revoked | expired",
    ),
):
    """Lista tokens emitidos con su estado."""
    console.print(
        f"[yellow]⚠️  pynet-admin token list (status={status}): "
        f"no implementado aún.[/yellow]"
    )


@token_app.command("revoke")
def token_revoke(
    token_id: str = typer.Argument(..., help="ID corto del token a revocar."),
):
    """Revoca un token que aún no ha sido consumido."""
    console.print(
        f"[yellow]⚠️  pynet-admin token revoke '{token_id}': "
        f"no implementado aún.[/yellow]"
    )
