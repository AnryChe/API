# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    link = scrapy.Field()
    site = scrapy.Field()
    curency = scrapy.Field()


class superjobItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    vac_name = scrapy.Field()
    salary = scrapy.Field()
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    link = scrapy.Field()
    site_name = scrapy.Field()
    curency = scrapy.Field()

class LMItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    item_name = scrapy.Field()
    item_photo_link = scrapy.Field()
    item_price = scrapy.Field()
    item_desc = scrapy.Field()
    link = scrapy.Field()
    site_name = scrapy.Field()
