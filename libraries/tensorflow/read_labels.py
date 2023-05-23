
import os
import json
import cv2 as cv


def get_img_size(fullpath) -> (int, int):
    image = cv.imread(fullpath)
    return image.shape[0], image.shape[1]


with open(os.path.join('datasets', 'labels.json')) as file:
    for record in json.load(file):
        filename = record["External ID"]
        bbox = record["Label"]["objects"][0]["bbox"]
        top, left, height, width = bbox['top'], bbox['left'], bbox['height'], bbox['width']
        # do stuff
        break
