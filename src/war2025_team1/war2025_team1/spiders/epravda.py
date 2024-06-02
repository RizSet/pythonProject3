import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class EpravdaSpider(scrapy.Spider):

    name = "epravda"
    allowed_domains = ["epravda.com.ua"]
    start_urls = ["1","2","3","4","5","6","7","8","9"]

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request("https://www.epravda.com.ua/tags/nerukhomist/page_" + link_url + "/", cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//div[@class="article__title"]')
        for article_link in content.xpath('.//a'):
            print(1)

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://www.epravda.com.ua" + item['article_url']
            print(item['article_url'])
            yield (item)
