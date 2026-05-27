import os
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from pathlib import Path

from src.http_client import fetch_binary
from src.constants import ONE_SECOND


def save_images(urls: list[str], save_dir: Path) -> None:
    save_dir.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(save_image, urls, repeat(save_dir))
    print(f"✅ {len(urls)} Images Are Saved!")


def save_image(url: str, save_dir: Path) -> None:
    file_name = os.path.basename(url)
    path = save_dir / file_name
    content = fetch_binary(url)
    print(f"⌛️ Waiting...")
    time.sleep(ONE_SECOND)
    path.write_bytes(content)
