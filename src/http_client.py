import requests


def fetch_html(url: str, timeout: int = 10) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def fetch_binary(url: str) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    return response.content
