import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os


class CustomImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        signs = request.meta['item']['signs'].replace(" ", "_")
        return signs + ".jpeg"
