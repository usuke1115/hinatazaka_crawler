from src.validator import validate_blog_url
from src.http_client import fetch_html
from src.parser import extract_img_tags
from src.parser import extract_img_urls


def set_url_for_crawl():
    print("Enter the URL to crawl.")
    blog_url = input()
    return blog_url


class HinatazakaBlogCrawler:
    def __init__(self, url: str):
        validate_blog_url(url)
        self.url = url

    def crawl_image_urls(self) -> list[str]:
        print(f"🚀 START to Crawl on {self.url}\n")
        html = fetch_html(self.url)
        img_tags = extract_img_tags(html)
        return extract_img_urls(img_tags)
