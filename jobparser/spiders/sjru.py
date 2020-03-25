# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class SjruSpider(scrapy.Spider):
    site_name = 'Superjob'
    allowed_domains = ['www.superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=']


    def parse(self, response: HtmlResponse):
        next_page = response.scc("a.f-test-link-dalshe::attr(@href)").extract_first()
        # next_page = response.css("a.HH-Pager-Controls-Next::attr(href)")
        if not next_page:
            yield
        else:
            yield response.follow(next_page, callback=self.parse)

        vac_list = response.css("div.f-test-vacancy-item a[target='_blank'])::elattr(href)").extract()
        for link in vac_list:
            yield response.follow(link, callback=self.vacansy_parse)


    def vacansy_parse(self, response: HtmlResponse):

        vac_name = response.xpath("//div[@class='_3mfro CuJz5 PlM3e _2JVkc _3LJqf']/text()").extract()[0]  # Экстракт не полностью помогает, выдает список. Если чезер css - проще и лучше
        salary = response.xpath("//span[@class='_3mfro _2Wp8I _31tpt f-test-text-company-item-salary PlM3e _2JVkc _2VHxz']/text()").extract()
        link = response.url()
        yield JobparserItem(vac_name=vac_name, salary=salary, link=link, site_name=self.site_name)

