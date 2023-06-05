import time
import scrapy
import random
import os
import math
import shutil


class CarsPlateSpider(scrapy.Spider):
    name = "plates"
    generic_url = ("https://tablica-rejestracyjna.pl/komentarze?p=",)
    start_urls = [
        f"https://tablica-rejestracyjna.pl/komentarze?p={num_page}"
        for num_page in range(201, 500)
    ]

    custom_settings = {
        "ITEM_PIPELINES": {"plate_scraper.pipelines.CustomImagesPipeline": 1},
        "IMAGES_STORE": "images",
    }

    def parse(self, response):
        for comment in response.css("div.comment"):
            if image_links := comment.css("span.text a[href]::attr(href)").getall():
                item = {
                    "signs": comment.css("span.plate a::text").get(),
                    "image_urls": [f"https:{link}" for link in image_links],
                }
                yield item
        # Generate random float and wait for the random delay
        time.sleep(random.uniform(1, 8))

    def closed(self, reason):
        print("Reformat images to chunks...")
        # call function after spider is closed
        split_to_chunks(500)


def split_to_chunks(chunk_size):
    # Set the path to the directory containing the images
    dir_path = "./images"

    # Get a list of all the image files in the directory
    img_files = [f for f in os.listdir(dir_path) if f.endswith(".jpeg")]

    num_chunks = math.ceil(len(img_files) / chunk_size)

    # Create the subdirectories
    for i in range(num_chunks):
        subdir_name = f"chunk_{i + 1}"
        subdir_path = os.path.join(dir_path, subdir_name)
        os.makedirs(subdir_path, exist_ok=True)

    # Move the images into the subdirectories
    for i, img_file in enumerate(img_files):
        subdir_name = f"chunk_{math.ceil((i + 1) / chunk_size)}"
        subdir_path = os.path.join(dir_path, subdir_name)
        img_src_path = os.path.join(dir_path, img_file)
        img_dest_path = os.path.join(subdir_path, img_file)
        shutil.move(img_src_path, img_dest_path)
