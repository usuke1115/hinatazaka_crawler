from src.crawler import HinatazakaBlogCrawler
from src.crawler import set_url_for_crawl
from src.downloader import save_images
from pathlib import Path


def main():
    blog_url = set_url_for_crawl()
    crawler = HinatazakaBlogCrawler(blog_url)
    img_urls = crawler.crawl_image_urls()
    save_images(img_urls, Path("images"))


if __name__ == "__main__":
    main()
