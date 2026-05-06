import os
from pathlib import Path
from src.http_client import fetch_binary


def save_images(urls: list[str], save_dir: Path) -> None:
    save_dir.mkdir(parents=True, exist_ok=True)

    for url in urls:
        file_name = os.path.basename(url)
        path = save_dir / file_name

        content = fetch_binary(url)
        path.write_bytes(content)
    print(f"✅ {len(urls)} Images Are Saved!")
