import re
import typing as t

BLOG_URL_PATTERN: t.Final = re.compile(
    r"^https://www\.hinatazaka46\.com/s/official/.*$"
)
BLOG_BODY_CLASS: t.Final = "c-blog-article__text"

ONE_SECOND: int = 1
