"""
pynet.cli.commands.sync
-----------------------
Comando `pynet sync`.

Hidrata el bloque BEGIN/END PYNET SYNC del .env de un proyecto existente,
usando un token nuevo. Pensado para devs que clonan un repo ajeno y
necesitan poder ejecutar el bot localmente.

Flujo:
  1. Busca `pynet.yaml` en el directorio actual.
  2. Lee de ahí el cliente esperado (ej: "colsubsidio").
  3. Resuelve el token (--token | PYNET_TOKEN).
  4. Consume el token contra el backend.
  5. Verifica que el cliente del token coincide con el del pynet.yaml.
  6. Escribe el bloque PYNET SYNC en .env (sin tocar variables manuales).
"""

import typer
from rich.console import Console
from rich.panel import Panel

from pynet.core.auth import resolve_token, token_source


console = Console()


def sync_command(
    token: str = typer.Option(
        None,
        "--token",
        help="Token de un solo uso emitido por un admin. Si no se pasa, "
             "se lee de PYNET_TOKEN.",
    ),
    path: str = typer.Option(
        ".",
        "--path",
        help="Ruta del proyecto a sincronizar. Por defecto: directorio actual.",
    ),
):
    """
    Hidrata el .env de un proyecto existente con credenciales frescas.

    [yellow]⚠️  Pendiente de implementación completa.[/yellow]
    """
    try:
        resolved = resolve_token(token)
        source = token_source(token)
        token_preview = f"{resolved[:12]}..." if len(resolved) > 12 else resolved
    except Exception as e:
        console.print(f"[red]❌ {e}[/red]")
        raise typer.Exit(code=1)

    console.print(
        Panel(
            f"[bold]Proyecto:[/bold] {path}\n"
            f"[bold]Token:[/bold]    {token_preview} [dim](origen: {source})[/dim]\n\n"
            f"[yellow]⚠️  El sync real aún no está implementado.[/yellow]\n"
            f"[dim]Próximos pasos:[/dim]\n"
            f"[dim]  1. Leer pynet.yaml del proyecto[/dim]\n"
            f"[dim]  2. Consumir token contra el backend[/dim]\n"
            f"[dim]  3. Verificar cliente coincide[/dim]\n"
            f"[dim]  4. Reescribir bloque BEGIN/END PYNET SYNC en .env[/dim]",
            title="[cyan]pynet sync[/cyan]",
            border_style="yellow",
        )
    )
