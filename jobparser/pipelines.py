# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re
from jobparser.items import superjobItem

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacansy_305


    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        self.salary_processing(item)
        collection.insert_one(item)
        return item


    def salary_processing(self, item):
        if not item.salary:
            salary_min = 0
            salary_max = 0
            curency = '₽'
        else:
            salary = item.salary
            if 'По договоренности' in salary:
                salary_min = 0
                salary_max = 0
                curency = '₽'
            elif 'от' in salary:
                salary_min = (re.findall('\d{3}.?\d{3}', salary))[0].replace(u'\xa0', u'')
                salary_max = 0
                curency = salary[-1]
            elif 'до\b' in salary:
                salary_max = (re.findall('\d{3}.?\d{3}', salary))[0].replace(u'\xa0', u'')
                salary_min = 0
                sj_curency = salary[-1]
            elif '—' in salary:
                sj_salary_price = re.findall('\d{3}.?\d{3}', salary)
                sj_parced_salary_max = sj_salary_price[1].replace(u'\xa0', u'')
                salary_min = sj_salary_price[0].replace(u'\xa0', u'')
                curency = salary[-1]
            yield superjobItem(vac_name=item.name, salary_max=salary_max, salary_min=salary_min, curency=curency, link=item.link, site_name=item.site_name) #не уверен насколько правильно, если здесь указать все поля, то лишние удалять не нужно?


class ItemsPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.lm_item_01


    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        pass
        collection.insert_one(item)
        return item


    def item_def_separator(self, item):
        for i in item.item_def:
            pass




