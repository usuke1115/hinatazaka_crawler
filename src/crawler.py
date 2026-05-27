from src.validator import validate_blog_url
from src.http_client import fetch_html
from src.parser import extract_img_tags
from src.parser import extract_img_urls


def set_url_for_crawl():
    print("Enter some URLs to crawl.")
    blog_urls = []
    while True:
        url = input()
        if url == "":
            return blog_urls
        blog_urls.append(url)


class HinatazakaBlogCrawler:
    def __init__(self, urls: list[str]):
        for url in urls:
            validate_blog_url(url)
        self.urls = urls

    def crawl_image_urls(self, url) -> list[str]:
        print(f"🚀 START to Crawl on {url}\n")
        html = fetch_html(url)
        img_tags = extract_img_tags(html)
        return extract_img_urls(img_tags)
