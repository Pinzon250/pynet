"""
pynet.admin.app
---------------
Entry point del CLI ADMIN (`pynet-admin`).

Comandos:
    pynet-admin client add        Registrar un nuevo cliente en el backend
    pynet-admin client list       Listar clientes registrados
    pynet-admin client show <s>   Mostrar datos de un cliente
    pynet-admin client remove <s> Eliminar un cliente

    pynet-admin token issue       Emitir un token de un solo uso
    pynet-admin token list        Listar tokens activos / consumidos
    pynet-admin token revoke <id> Revocar un token aún no consumido
"""

import typer
from rich.console import Console

from pynet.__version__ import __version__
from pynet.admin.commands.client import client_app
from pynet.admin.commands.token import token_app


console = Console()


app = typer.Typer(
    name="pynet-admin",
    help="CLI administrativo de pynet — gestión de clientes y tokens.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",
)


def _version_callback(value: bool) -> None:
    if value:
        console.print(
            f"[bold magenta]pynet-admin[/bold magenta] versión "
            f"[green]{__version__}[/green]"
        )
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version", "-v",
        help="Muestra la versión y termina.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """CLI administrativo de pynet."""
    pass


app.add_typer(client_app, name="client", help="Gestionar clientes registrados.")
app.add_typer(token_app, name="token", help="Emitir y administrar tokens.")


if __name__ == "__main__":
    app()
