import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class MinfinSpider(scrapy.Spider):

    name = "minfin"
    allowed_domains = ["minfin.com.ua"]
    # start_urls = ["1","2","3","4","5","6","7","8","9","10", "11", "12", "13", "14"]

    def start_requests(self):
        # for link_url in self.start_urls:
        for number_url in range(1, 27, 1):
            url = f"https://minfin.com.ua/ua/realty/news/{number_url}/"
            print(number_url)
            request = Request(url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//ul[@class="items"]/li')
        for article_link in content.xpath('.//a'):
            print(1)

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://minfin.com.ua" + item['article_url']
            print(item['article_url'])
            yield (item)
