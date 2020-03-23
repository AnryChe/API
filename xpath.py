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
        # print(response)
        tree = html.fromstring(response)
        news_data = {}
        if link == 'https://korrespondent.net':
            source_name = 'Корреспондент'
            news = tree.xpath("//div[@class='time-articles']//*")
            for new in news:
                news_name = news.xpath(".//a/text()")
                print(news_name)
                news_time = news.xpath("//div[@class='time-articles']//div[@class='article__time']//text()")
                news_link = tree.xpath("//div[@class='time-articles']//a/@href")
        elif link == 'https://www.rbc.ua':
            pass

            # news_data['source'] = source_name
            # news_data['time'] = news_times
            # news_data['link'] = news_links[news_name]
            # news_list.append(news_data)


get_html(main_links)
print(news_list)
def get_korr(tree):
    # name = tree.xpath("/div[@class='time-articles']//div[@class='time-articles']/a/text()")
    pass