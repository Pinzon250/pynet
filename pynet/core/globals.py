from datetime import datetime
import sys
from pathlib import Path

FW_NAME = "pynet"
FW_VERSION = "0.1.0"
FW_ROOT = Path(__file__).parent.parent

def build_global_context(project_name: str, author: str | None = None) -> dict:
    return {
        "project_name": project_name,
        "project_slug": project_name.lower().replace(" ", "_"),
        "author": author or "unknown",
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "framework": {
            "name": FW_NAME,
            "version": FW_VERSION
        }
    }