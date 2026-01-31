from pathlib import Path
from typing import Protocol
from framework.core.context import ProjectContext
from framework.utils.files import ensure_dir, write_file

def generate_project(context: ProjectContext):
    validate_context(context)
    if context.project_path.exists():
        if not context.force:
            raise FileExistsError(
                f"El directorio '{context.project_path}' ya existe"
            )
        
    create_structure(context)
    render_templates(context)

def validate_context(context: ProjectContext):
    if not context.name.isidentifier():
        raise ValueError(
            "Nombre de proyecto invalido"
        )
    
    if context.template not in ["basic", "rpa", "scripts"]:
        raise ValueError(
            "Template no soportado"
        )
    
def create_structure(context: ProjectContext):
    dirs = [
        context.project_path / "app",
        context.project_path / "app" / "services"
    ]

    if context.features.get("scripts"):
        dirs.append(context.project_path / "scripts")

    if context.features.get("tests"):
        dirs.append(context.project_path / "tests")

    for d in dirs:
        ensure_dir(d, context.dry_run)

def render_templates(context: ProjectContext):
    pass