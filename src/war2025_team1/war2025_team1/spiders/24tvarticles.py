import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import War2025Team1Item


class TvSpider(scrapy.Spider):
    name = "24tvarticles"

    def start_requests(self):

        file_path = './24tv.json'
        with open(file_path, 'r', encoding='cp1251') as file:
            data = json.load(file)

        for link_url in data:
            print(link_url)
            request = Request(link_url['article_url'], cookies={'store_language': 'ua'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2025Team1Item()
        item['article_url'] = response.url
        item['article_uuid'] = hashlib.sha256(str(response.url).encode('utf-8')).hexdigest()
        item['article_id'] = response.url.split("_n")[-1]

        first_step = response.xpath(
            '//app-default-news[@class="news-wrapper"]').extract_first()
        second_step = scrapy.Selector(text=first_step).xpath(
            './/div[@class="top-news-info"]').extract_first()
        date = scrapy.Selector(text=second_step).xpath('.//span[@class="date"]/text()').extract_first()

        item['article_datetime'] = date

        item['article_title'] = scrapy.Selector(text=first_step).xpath(
            '//h1[@class="article-title"]/text()').extract()

        item['article_text'] = response.xpath(
            '//app-default-news[@class="news-wrapper"]//app-news-content//p//text()').extract()

        yield (item)
