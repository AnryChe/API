# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import LMItem

class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru/catalogue/plastikovye-okna']
    start_urls = ['http://leroymerlin.ru/catalogue/plastikovye-okna/']


    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-page]/@href").extract_first() # Находим первую страничку с товарами
        print(next_page)
        if not next_page:
            yield
        else:
            yield response.follow(next_page, callback=self.parse)

        items_list = response.xpath("//a[@class='link-wrapper']/@href").extract() # Создаем список ссылок на страницы
        print(items_list)

        for link in items_list: # Перебираем ссылки и генерим ответ для следующей функции
            print(link)
            yield response.follow(link, callback=self.item_parse)

    def item_parse(self, response: HtmlResponse):
        item_name = response.xpath("//h1[@itemprop='name']/text").extract()
        print(item_name)
        # Собираем пока просто описание товара, характеристики соберу позднее
        item_desc = response.xpath("//*[@class='section__vlimit']//p/text()").extract()
        item_def = response.xpath("//*[@class='def-list']").extract()
        item_photo_link = response.xpath("//img[@alt='product image']/@data-origin").extract()
        item_price = response.xpath("//span[@slot='price']/text()").extract()
        link = response.url()
        yield LMItem(item_name=item_name, item_price=item_price, link=link, site_name=self.site_name, item_desc=item_desc, item_def=item_def, item_photo_link=item_photo_link)


