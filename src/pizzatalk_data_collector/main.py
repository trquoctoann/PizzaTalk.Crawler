from datetime import datetime, timedelta

from crawler.crawler import Crawler
from generator.generator import ChatGPTGenerator
from labeller.aggregator import aggregate_today_response

# crawler = Crawler()
# areas = crawler.crawl("area")
# stores = crawler.crawl("store")
# categories = crawler.crawl("category")
# deals = crawler.crawl("deal")
# products = crawler.crawl("product")

chatgpt = ChatGPTGenerator(
    chrome_path='"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
)
chatgpt.auto_login()
chatgpt.generate_for_predefined_prompts()
