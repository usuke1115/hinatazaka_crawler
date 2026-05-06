from bs4 import BeautifulSoup
from bs4 import Tag
from src.constants import BLOG_BODY_CLASS
from src.exceptions import BlogContentNotFoundError


def extract_img_tags(html: str) -> list[Tag]:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find("div", class_=BLOG_BODY_CLASS)

    if content is None:
        raise BlogContentNotFoundError(
            f"ブログ本文が見つかりません (class={BLOG_BODY_CLASS})"
        )

    return content.find_all("img")


def extract_img_urls(img_tags: list[Tag]) -> list[str]:
    return [tag["src"] for tag in img_tags if tag.has_attr("src")]
