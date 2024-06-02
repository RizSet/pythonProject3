import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class MinfinSpider(scrapy.Spider):
    name = "minfinarticles"

    def start_requests(self):

        file_path = './minfin.json'
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
            '//div[@class="header-info_attrs"]/span[@class="data"]/text()').extract())

        item['article_datetime'] = response.xpath(
            '//div[@class="header-info_attrs"]/span[@class="data"]/text()').extract()

        item['article_title'] = response.xpath(
            '//h1[@itemprop="name"]/text()').extract()

        item['article_text'] = response.xpath(
            '//div[@class="progressive-news-text anons"]/p/text()').extract() +response.xpath(
            '//div[@class="progressive-news-text"]/div/p/text()').extract()+ response.xpath(
            '//div[@class="progressive-news-text"]/p/text()').extract()

        print(item)

        yield (item)
