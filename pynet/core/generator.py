from pathlib import Path
from tempfile import template
from pynet.core.context import ProjectContext
from pynet.utils.files import ensure_dir, write_file
from jinja2 import Environment, FileSystemLoader
import re

def generate_project(context: ProjectContext):
    validate_context(context)
    if context.project_path.exists() and not context.force:
        raise FileExistsError(
            f"El directorio '{context.project_path}' ya existe"
        )

    create_structure(context)

    render_templates(
        template_dir=get_template_path(context.template),
        target_dir=context.project_path,
        context=build_render_context(context),
        dry_run=context.dry_run
    )

def validate_context(context: ProjectContext):
    if not context.name.isidentifier():
        raise ValueError(
            "Nombre de proyecto invalido"
        )
    
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]+$", context.name):
        raise ValueError("Nombre de proyecto inválido")
    
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

def render_templates(
    template_dir: Path,
    target_dir: Path,
    context: dict,
    dry_run: bool = False
):
    
    if not template_dir.exists():
        raise FileNotFoundError(f"Template '{template_dir}' no existe")

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=False
    )

    for template_path in template_dir.rglob("*.j2"):
        relative_path = template_path.relative_to(template_dir)

        template_name = relative_path.as_posix()

        output_path = target_dir / relative_path.with_suffix("")

        if dry_run:
            print(f"[DRY-RUN] Crear archivo: {output_path}")
            continue

        output_path.parent.mkdir(parents=True, exist_ok=True)

        template = env.get_template(template_name)
        content = template.render(**context)

        output_path.write_text(content, encoding="utf-8")
    
        
def get_template_path(template_name: str) -> Path:
    base = Path(__file__).parent.parent / "templates"
    return base / template_name

def build_render_context(context: ProjectContext) -> dict:
    return {
        "project_name": context.name,
        "db_driver": context.db,
        "features": context.features
    }
    