from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient


driver = webdriver.Firefox()


def get_messages_ukrnet(login, password):
    driver.get('https://mail.ukr.net/')
    assert "Пошта @ ukr.net" in driver.title

    elem = driver.find_element_by_id('id-l')
    elem.send_keys(login)
    time.sleep(1)

    elem = driver.find_element_by_id('id-p')
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    return driver


def spam_list(driver):
    try:
        profile = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, '10003'))
        )
        driver.get(profile.get_attribute('href'))
        time.sleep(2)
        links = driver.find_elements_by_class_name('msglist__row_href')
        return links
    finally:
        pass

def get_message(links):

    for i in links:
        link = i.get_attribute('href')
        driver.get(link)
        time.sleep(5)
# ДВА ВАРИАНТА, С ВАЙТОМ И БЕЗ. Вайт вываливается в эксепт, хотя элемент на страничке есть  (xpath находит по  //*[@class='readmsg__head-contact main']
# Вариант 1, с wait:

        try:
            from_who = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'readmsg__head-contact main'))
            )
        except:
            print('элемент не обнаружен')
        finally:
            pass
        from_who = from_who.get_attribute('data-email')


        shipping_data = driver.find_element_by_class_name('readmsg__head-date')
        theme_letter = driver.find_element_by_class_name('readmsg__subject')
        body_letter = driver.find_element_by_class_name('readmsg__body')
        got_letter = {'From':from_who,
                       'Data':shipping_data,
                       'theme':theme_letter,
                       'Letter':body_letter}
        un_base.insert_one(got_letter)


my_login = 'kjdfshgmnjkew'
my_password = '22Renegatspekulant22'
client = MongoClient('localhost', 27017)
un_base = client.ukr_net

get_message(spam_list(get_messages_ukrnet(my_login, my_password)))

