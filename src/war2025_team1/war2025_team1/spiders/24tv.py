import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class TvSpider(scrapy.Spider):

    name = "24tv"
    allowed_domains = ["realestate.24tv.ua"]

    def start_requests(self):
        for number_url in range(0, 1290, 14):
            url = f"https://realestate.24tv.ua/analitika-rinku_tag7714/fromnews{number_url}/"
            request = Request(url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        content = response.xpath('//div[@class="news-title"]//h3')
        for article_link in content.xpath('.//a'):

            item['article_url'] = article_link.xpath('.//@href').extract_first()
            item
            # if item['article_url'].startswith("http"):
            #     continue
            item['article_url'] = item['article_url']
            print(item['article_url'])
            yield (item)

