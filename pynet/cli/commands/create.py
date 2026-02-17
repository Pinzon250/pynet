import typer
from pathlib import Path
from pynet.core.generator import generate_project
from pynet.core.context import ProjectContext
from pynet.core.templates import list_templates
from pynet.cli.utils.interactive import select_template

create_app = typer.Typer(help="Comandos de creación de proyecto")


@create_app.command("app")
def create(
    project_name: str,
    template: str = typer.Option(
        None,
        help="Template base (si no se pasa, se muestra selector interactivo)",
    ),
    path: str = typer.Option(".", help="Ruta destino"),
    db: str = typer.Option("none", help="Motor de BD"),
    with_scripts: bool = typer.Option(False),
    with_test: bool = typer.Option(True),
    with_env: bool = typer.Option(True),
    force: bool = typer.Option(False),
    dry_run: bool = typer.Option(False),
):
    # --- selección interactiva si no se pasa template ---
    if template is None:
        templates = list_templates()

        if not templates:
            typer.secho("No hay templates disponibles", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        template = select_template(templates)

    typer.secho(
        f"Creando plantilla {template}",
        fg=typer.colors.GREEN,
    )

    context = ProjectContext(
        name=project_name,
        template=template,
        path=Path(path),
        db=db,
        features={
            "scripts": with_scripts,
            "test": with_test,
            "env": with_env,
        },
        force=force,
        dry_run=dry_run,
    )

    generate_project(context)
