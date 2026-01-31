from pathlib import Path

def ensure_dir(path: Path, dry_run: bool):
    if dry_run:
        print(f"[DRY-RUN] mkdir {path}")
        return
    path.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str, dry_run: bool):
    if dry_run:
        print(f"[DRY-RUN] write {path}")
        return
    path.write_text(content, encoding="utf-8")