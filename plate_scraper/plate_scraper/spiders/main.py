from urllib.parse import to_bytes
import scrapy
import hashlib
from scrapy.pipelines.images import ImagesPipeline
import logging
from scrapy.extensions.feedexport import FeedExporter


# scrapy runspider main.py -o quotes.json


class CarsPlateSpider(scrapy.Spider):
    name = "plates"
    start_urls = [
        'https://tablica-rejestracyjna.pl/komentarze',
    ]

    custom_settings = {
        'ITEM_PIPELINES': {'plate_scraper.pipelines.CustomImagesPipeline': 1},
        'IMAGES_STORE': 'images',
        'LOG_LEVEL': logging.DEBUG,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'items.json',
    }

    def parse(self, response):
        for response in response.css('div.comment'):
            image_url = "https:" + response.css('span.text a::attr(href)').get()
            item = {
                'signs': response.css('span.plate a::text').get(),
                'image_urls': [image_url],
            }
            yield item

