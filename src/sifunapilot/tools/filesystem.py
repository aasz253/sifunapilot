from pathlib import Path
from typing import Any


class FileSystemTools:
    async def list_files(self, path: str = ".", **kwargs: Any) -> str:
        try:
            p = Path(path).expanduser().resolve()
            if not p.exists():
                return f"✗ Path does not exist: {path}"
            files = sorted([f.name for f in p.iterdir()])
            if not files:
                return f"✓ {path} is empty"
            return f"✓ Files in {path}: {', '.join(files[:20])}"
        except Exception as e:
            return f"✗ Error: {e}"

    async def read_file(self, path: str, **kwargs: Any) -> str:
        try:
            p = Path(path).expanduser().resolve()
            content = p.read_text()
            return f"✓ Read {path} ({len(content)} chars)"
        except Exception as e:
            return f"✗ Error: {e}"

    async def write_file(self, path: str, content: str, **kwargs: Any) -> str:
        try:
            p = Path(path).expanduser().resolve()
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
            return f"✓ Wrote to {path}"
        except Exception as e:
            return f"✗ Error: {e}"

    async def copy_file(self, src: str, dst: str, **kwargs: Any) -> str:
        try:
            from shutil import copy2

            copy2(src, dst)
            return f"✓ Copied {src} to {dst}"
        except Exception as e:
            return f"✗ Error: {e}"

    async def move_file(self, src: str, dst: str, **kwargs: Any) -> str:
        try:
            from shutil import move

            move(src, dst)
            return f"✓ Moved {src} to {dst}"
        except Exception as e:
            return f"✗ Error: {e}"

    async def create_dir(self, path: str, **kwargs: Any) -> str:
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return f"✓ Created directory: {path}"
        except Exception as e:
            return f"✗ Error: {e}"
