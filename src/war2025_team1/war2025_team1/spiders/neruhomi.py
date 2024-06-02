import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class NerukhomiSpider(scrapy.Spider):

    name = "nerukhomi"
    allowed_domains = ["nerukhomi.ua"]
    start_urls = ["1","2","3","4","5","6","7","8","9"]

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request("https://nerukhomi.ua/ukr/news/?sectionID=469&page=" + link_url ,
                              cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//div[@class="newsList_cardsList"]/article')

        for article_link in content:

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            # if item['article_url'].startswith("http"):
            #     continue
            # item['article_url'] = item['article_url']
            print(item['article_url'])
            yield (item)
