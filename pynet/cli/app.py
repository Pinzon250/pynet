import typer
from pynet.cli.commands.create import create_app

app = typer.Typer(
    help="CLI principal del framework pynet"
)

app.command()(create_app)
