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
main_links = {r'https://korrespondent.net': 'time-articles', r'https://www.rbc.ua': 'content-section', r'https://sd.ua/news': 'item-list'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0'}

news_list = []
def get_html(main_links):
    for link in main_links.keys():

        div_class = main_links.get(link)
        response = requests.get(link, headers = headers).text
        tree = html.fromstring(response)
        if link == 'https://korrespondent.net':
            source_name = 'Корреспондент'
            news_items = tree.xpath("//div[@class='time-articles']/*")
            print(len(news_items))
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
            pass
        print(news_list)


get_html(main_links)
