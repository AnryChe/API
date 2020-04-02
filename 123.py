"""1 вариант
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайта superjob.ru и hh.ru.
Приложение должно анализировать несколько страниц сайта(также вводим через input или аргументы).
Получившийся список должен содержать в себе минимум:
●	Наименование вакансии
●	Предлагаемую зарплату (отдельно мин. и и отдельно макс.)
●	Ссылку на саму вакансию
●	Сайт откуда собрана вакансия
По своему желанию можно добавить еще параметры вакансии (например работодателя и расположение). Данная структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
"""


import requests
import json
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0'}
sites = {'SuperJob': 'https://russia.superjob.ru/', 'HeadHunter':'https://hh.ru/'}
get_requests = {'SuperJob': 'vacancy/search/?keywords=', 'HeadHunter':'search/vacancy?Vacancy&text='}



vacansy = 'python'
vacansys = []


main_link_sj = sites['SuperJob']+get_requests['SuperJob']+vacansy

response = requests.get(main_link_sj, headers = headers)
parced_html = bs(response.text, 'lxml')



sj_div_class = '_3zucV f-test-vacancy-item undefined RwN9e _3tNK- _1I1pc'
sj_div_class_vac_name = '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'
sj_div_class_salary = '_3mfro _2Wp8I _31tpt f-test-text-company-item-salary PlM3e _2JVkc _2VHxz'

# Переменные наименования вакансии, зарплаты:
sj_parced_name = parced_html.find('div', {'class': sj_div_class_vac_name}).getText()
sj_parced_salary = parced_html.find('span', {'class': sj_div_class_salary})
if not sj_parced_name:
    print('Вакансия не найдена')
else:
    if not sj_parced_salary:
        sj_parced_salary_min = 0
        sj_parced_salary_max = 0
        sj_curency = '₽'
    else:
        sj_parced_salary_txt = sj_parced_salary.getText()
        # print(re.findall('до$', sj_parced_salary_txt))
        if 'По договоренности' in sj_parced_salary_txt:
            # print('По договорённости')
            sj_parced_salary_min = 0
            sj_parced_salary_max = 0
            sj_curency = '₽'
        elif 'от' in sj_parced_salary_txt:
            # print('от')
            sj_parced_salary_min = (re.findall('\d{3}.?\d{3}', sj_parced_salary_txt))[0].replace(u'\xa0', u'')
            sj_parced_salary_max = 0
            sj_curency = sj_parced_salary_txt[-1]
        elif 'до' in sj_parced_salary_txt:
            print('до')
            sj_parced_salary_max = sj_parced_salary_txt
            sj_parced_salary_min = 0
            sj_curency = sj_parced_salary_txt[-1]
        elif '—' in sj_parced_salary_txt:
            # print('-')
            sj_parced_salary_price = re.findall('\d{3}.?\d{3}', sj_parced_salary_txt)
            sj_parced_salary_max = sj_parced_salary_price[1].replace(u'\xa0', u'')
            sj_parced_salary_min = sj_parced_salary_price[0].replace(u'\xa0', u'')
            sj_curency = sj_parced_salary_txt[-1]
        else:
            print('Что то пошло не так...')
        print('Сайт: ', 'Суперджоб', 'Вакансия: ', sj_parced_name, '. Зарплата от', sj_parced_salary_min, 'до',
              sj_parced_salary_max, sj_curency)
    vac_data = {}
    vac_data['Site'] = sites['SuperJob']
    vac_data['name'] = sj_parced_name
    vac_data['salary_min'] = sj_parced_salary_min
    vac_data['salary_max'] = sj_parced_salary_max
    vac_data['salary_link'] = page_sj
    vacansys.append(vac_data)


print(vacansys)