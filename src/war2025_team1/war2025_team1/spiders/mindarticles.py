import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class MindSpider(scrapy.Spider):
    name = "mindarticles"

    def start_requests(self):

        file_path = './mind.json'
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

        item['article_datetime'] = response.xpath(
            '//span[@class="post__info__date"]/text()').extract()

        item['article_title'] = response.xpath(
            '//h1[@class="post__title"]/text()').extract()
        #
        item['article_text'] = (response.xpath(
            '//div[@class="post__text"]/p/text()').extract())

        print(item)

        yield (item)
