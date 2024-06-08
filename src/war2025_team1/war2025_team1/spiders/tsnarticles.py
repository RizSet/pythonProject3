import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class TSNSpider(scrapy.Spider):
    name = "tsnarticles"

    def start_requests(self):

        file_path = './tsn.json'
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


        date = response.xpath(
                '//dd[@class="c-bar__label"]//time/text()').extract_first()

        # if not any(year in date for year in ["2021", "2022", "2023"]):
        #     date += " 2024"
        #     item['article_datetime'] = date

        item['article_datetime'] = date
        # print(item['article_datetime'])
        #
        item['article_title'] = response.xpath(
            '//h1[@class="c-card__title"]//span/text()').extract()
        # # #
        item['article_text'] = response.xpath(
            '//div[@data-content]//p/text()').extract()

        # print(item)

        yield (item)
