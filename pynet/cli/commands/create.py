import typer
from pathlib import Path
from pynet.core.generator import generate_project
from pynet.core.context import ProjectContext

app = typer.Typer()

@app.command()
def create_app(
    project_name: str,
    template: str = typer.Option("basic", help="Template base"),
    path: str = typer.Option(".", help="Ruta destino"),
    db: str = typer.Option("none", help="Motor de BD"),
    with_scripts: bool = typer.Option(False),
    with_test: bool = typer.Option(True),
    with_env: bool = typer.Option(True),
    force: bool = typer.Option(False),
    dry_run: bool = typer.Option(False)
):
    context = ProjectContext(
        name=project_name,
        template=template,
        path=Path(path),
        db=db,
        features={
            "scripts": with_scripts,
            "test": with_test,
            "env": with_env
        },
        force=force,
        dry_run=dry_run
    )

    generate_project(context)