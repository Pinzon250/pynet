from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass
class ProjectContext:
    name: str
    template: str
    path: Path
    db: str
    features: Dict[str, bool]
    force: bool = False
    dry_run: bool = False

    @property
    def project_path(self) -> Path:
        return self.path / self.name    