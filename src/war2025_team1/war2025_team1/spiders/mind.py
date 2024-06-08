import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class MindSpider(scrapy.Spider):

    name = "mind"
    allowed_domains = ["mind.ua"]
    # start_urls = ["1","2","3","4","5","6","7","8","9"]

    def start_requests(self):
        for number_url in range(1, 27, 1):
            url = f"https://mind.ua/realestate?p={number_url}"
            print(url)
            request = Request(url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//div[@class="article__title"]')
        for article_link in content.xpath('.//a'):
            print(1)

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("https://mind.ua/news") or item['article_url'].startswith("https://mind.ua/publications"):
                item['article_url'] = item['article_url']
            else:continue
            print(item['article_url'])
            yield (item)
