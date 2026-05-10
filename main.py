from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from pathlib import Path

from src.crawler import HinatazakaBlogCrawler, set_url_for_crawl
from src.downloader import save_images


def main():
    blog_urls = set_url_for_crawl()
    crawler = HinatazakaBlogCrawler(blog_urls)
    image_urls = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        image_urls = list(executor.map(crawler.crawl_image_urls, blog_urls))
    save_images(list(chain.from_iterable(image_urls)), Path("images"))


if __name__ == "__main__":
    main()
