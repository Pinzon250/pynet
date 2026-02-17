from pathlib import Path

def list_templates() -> list[str]:
    base = Path(__file__).parent.parent / "templates"

    if not base.exists():
        return []

    return sorted(
        d.name
        for d in base.iterdir()
        if d.is_dir()
    )