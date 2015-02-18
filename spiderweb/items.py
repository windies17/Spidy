# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class SpidyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() # if it throws an error delete the scrapy.
    time = scrapy.Field()
    speaker = scrapy.Field()
    description = scrapy.Field()