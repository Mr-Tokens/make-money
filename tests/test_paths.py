import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS_DIR = ROOT / "tests" / "artifacts"


def make_artifact_dir(prefix: str) -> Path:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=prefix, dir=ARTIFACTS_DIR))


def remove_artifact_dir(path: Path) -> None:
    if not path.is_relative_to(ARTIFACTS_DIR):
        raise ValueError(f"Refusing to remove non-test artifact path: {path}")
    shutil.rmtree(path, ignore_errors=True)
