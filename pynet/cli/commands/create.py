"""
pynet.cli.commands.create
-------------------------
Subcomandos para crear nuevos proyectos desde plantillas.

Uso (cuando esté implementado):
    pynet create app MiBot --template rpa --token pynet_ot_xxx
"""

import typer
from rich.console import Console
from rich.panel import Panel

from pynet.core.auth import resolve_token, token_source


create_app = typer.Typer(
    help="Crear nuevos proyectos desde plantillas.",
    no_args_is_help=True,
)
console = Console()


@create_app.command("app")
def create_app_cmd(
    project_name: str = typer.Argument(
        ...,
        help="Nombre del proyecto (identificador Python válido).",
    ),
    template: str = typer.Option(
        None,
        "--template", "-t",
        help="Plantilla base: basic | rpa (si no se pasa, se preguntará).",
    ),
    token: str = typer.Option(
        None,
        "--token",
        help="Token de un solo uso emitido por un admin. Si no se pasa, "
             "se lee de PYNET_TOKEN.",
    ),
):
    """
    Crea un nuevo proyecto desde una plantilla.

    El token se consume al ejecutar este comando (modelo de un solo uso).
    Si necesitas crear otro proyecto, solicita otro token.

    [yellow]⚠️  Pendiente de implementación completa.[/yellow]
    """
    # Por ahora solo resolvemos el token y lo mostramos.
    # La generación real del proyecto se implementa en el paso 5.
    try:
        resolved = resolve_token(token)
        source = token_source(token)
        # Mostrar solo los primeros 12 chars del token por seguridad
        token_preview = f"{resolved[:12]}..." if len(resolved) > 12 else resolved
    except Exception as e:
        console.print(f"[red]❌ {e}[/red]")
        raise typer.Exit(code=1)

    console.print(
        Panel(
            f"[bold]Proyecto:[/bold]   {project_name}\n"
            f"[bold]Template:[/bold]   {template or '[dim](no especificado)[/dim]'}\n"
            f"[bold]Token:[/bold]      {token_preview} [dim](origen: {source})[/dim]\n\n"
            f"[yellow]⚠️  La creación real aún no está implementada.[/yellow]\n"
            f"[dim]Próximo paso: implementar el generator con Jinja2.[/dim]",
            title="[cyan]pynet create app[/cyan]",
            border_style="yellow",
        )
    )
