import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class EpravdaSpider(scrapy.Spider):
    name = "epravdaarticles"

    def start_requests(self):

        file_path = './epravda.json'
        with open(file_path, 'r', encoding='cp1251') as file:
            data = json.load(file)

        for link_url in data:
            print(link_url)
            request = Request(link_url['article_url'], cookies={'store_language': 'ua'}, callback=self.parse)
            yield request

    def parse(self, response):
        print(1)
        item = War2025Team1Item()
        print(2)
        item['article_url'] = response.url
        item['article_uuid'] = hashlib.sha256(str(response.url).encode('utf-8')).hexdigest()
        item['article_id'] = response.url.split("/")[-1]

        print(response.xpath(
            '//h1[@class="post__title"]/text()').extract())

        item['article_datetime'] = response.xpath(
            '//div[@class="post__time"]/text()').extract()

        item['article_title'] = response.xpath(
            '//h1[@class="post__title"]/text()').extract()

        item['article_text'] = (response.xpath(
            '//div[@class="post__text"]/p/text()').extract() +
                                response.xpath(
            '//div[@class="post__text"]/p/span/text()').extract())

        print(item)

        yield (item)
