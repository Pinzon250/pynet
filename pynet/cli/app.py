"""
pynet.cli.app
-------------
Entry point del CLI del DEV. Comandos principales:

    pynet create app <name> [--template T] --token <T>
        Crea un proyecto nuevo desde una plantilla.

    pynet sync --token <T>
        Hidrata el .env de un proyecto ya existente (clonado de Git).
        Lee pynet.yaml para saber qué cliente usar.

Para gestión de clientes y emisión de tokens, ver `pynet-admin` (CLI separado).
"""

import typer
from rich.console import Console

from pynet.__version__ import __version__
from pynet.cli.commands.create import create_app
from pynet.cli.commands.sync import sync_command


console = Console()


app = typer.Typer(
    name="pynet",
    help="Framework CLI para proyectos Python (especialmente RPA) en NetApplications.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",
)


def _version_callback(value: bool) -> None:
    if value:
        console.print(
            f"[bold cyan]pynet[/bold cyan] versión [green]{__version__}[/green]"
        )
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version", "-v",
        help="Muestra la versión de pynet y termina.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """Framework CLI para proyectos Python."""
    pass


# ── Registro de comandos ──────────────────────────────────────────────────
# `create` es un sub-app (tiene varios comandos: `pynet create app`, futuro
# `pynet create script`, etc.).
# `sync` es un comando único, se registra como command, no como typer anidado.
app.add_typer(
    create_app,
    name="create",
    help="Crear nuevos proyectos desde plantillas.",
)
app.command(
    name="sync",
    help="Hidratar el .env de un proyecto existente (clonado de Git) con un token nuevo.",
)(sync_command)


if __name__ == "__main__":
    app()
