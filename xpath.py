'''
Написать приложение, которое собирает основные новости с сайтов. Для парсинга использовать XPath. Структура данных должна содержать:
●	название источника;
●	наименование новости;
●	ссылку на новость;
●	дата публикации.

'''


import requests
from pprint import pprint
from lxml import html
from pymongo import MongoClient

main_links = {r'https://korrespondent.net': 'time-articles', r'https://www.rbc.ua': 'content-section', r'https://www.ukr.net/ru': 'feed'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0'}

news_list = []
def get_html(main_links):
    for link in main_links.keys():
        div_class = main_links.get(link)
        response = requests.get(link, headers = headers).text
        tree = html.fromstring(response)
        news_items = tree.xpath("//div[@class='{0}']/*".format(div_class))
        if link == 'https://korrespondent.net':
            source_name = 'Корреспондент'
            for i in news_items:
                news_data = {}
                news_name = i.xpath(".//a/text()")
                news_time = i.xpath(".//div[@class='article__time']//text()")
                news_link = i.xpath(".//a/@href")
                news_data['source'] = source_name
                news_data['name'] = news_name
                news_data['time'] = news_time
                news_data['link'] = news_link
                news_list.append(news_data)

        elif link == 'https://www.rbc.ua':
            source_name = 'РБК'
            for i in news_items:
                news_data = {}
                news_name = i.xpath(".//a/text()")
                news_time = i.xpath(".//span[@class='time']//text()")
                news_link = i.xpath(".//a/@href")
                news_data['source'] = source_name
                news_data['name'] = news_name
                news_data['time'] = news_time
                news_data['link'] = news_link
                news_list.append(news_data)

        elif link == 'https://www.ukr.net/ru':
            news_items = tree.xpath("//div[@class='feed__item--title']".format(div_class))
            source_name = 'УКР.NET'
            for i in news_items:
                news_data = {}
                news_name = i.xpath(".//a/text()")
                news_time = i.xpath(".//span[@class='time']//text()")
                news_link = i.xpath(".//a/@href")
                news_data['source'] = source_name
                news_data['name'] = news_name
                news_data['time'] = news_time
                news_data['link'] = news_link
                news_list.append(news_data)



get_html(main_links)
pprint(news_list)
client = MongoClient('localhost', 27017)
db = client['news_database']
db.collection.insertMany(news_list)
