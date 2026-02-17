import typer
from pynet.cli.commands.create import create_app

app = typer.Typer(help="CLI principal del framework pynet")

app.add_typer(create_app, name="create")