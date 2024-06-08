import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class TSNSpider(scrapy.Spider):

    name = "tsn"
    allowed_domains = ["tsn.ua"]

    def start_requests(self):
        for number_url in range(1, 9, 1):
            url = f"https://tsn.ua/tags/%D0%BD%D0%B5%D1%80%D1%83%D1%85%D0%BE%D0%BC%D1%96%D1%81%D1%82%D1%8C/page-{number_url}"
            print(url)
            request = Request(url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//h3[@class="c-card__title  "]')
        for article_link in content.xpath('.//a'):
            print(1)

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            # if item['article_url'].startswith("https://mind.ua/news") or item['article_url'].startswith("https://mind.ua/publications"):
            item['article_url'] = item['article_url']
            # else:continue
            print(item['article_url'])
            yield (item)
