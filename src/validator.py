from src.constants import BLOG_URL_PATTERN
from src.exceptions import InvalidBlogUrlError


def validate_blog_url(url: str) -> None:
    if not BLOG_URL_PATTERN.search(url):
        raise InvalidBlogUrlError(f"The URL is not Hinatazaka Blog URL: {url}")
