from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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
        print(link)
        driver.get(link)
        from_who = driver.find_elements_by_class_name('readmsg__head-contact main').get_attribute('data-email')
        shipping_data = driver.find_elements_by_class_name('readmsg__head-date')
        theme_letter = driver.find_elements_by_class_name('readmsg__subject')
        body_letter = driver.find_elements_by_class_name('readmsg__body')





my_login = 'kjdfshgmnjkew'
my_password = '22Renegatspekulant22'

get_message(spam_list(get_messages_ukrnet(my_login, my_password)))
    # yield pass
#
# //a[@class='msglist__row']

# profile = driver.find_element_by_xpath("//a[@class='avatar']")  #@href?
# driver.get(profile.get_attribute('href'))
#

# edit_profile = driver.find_element_by_class_name('text-sm')
# driver.get(edit_profile.get_attribute('href'))
#
# name = driver.find_element_by_name('user[first_name]')
# name.send_keys(Keys.CONTROL + 'a')
# name.send_keys(Keys.BACK_SPACE)
#
# gender = driver.find_element_by_name('user[gender]')
# # options = gender.find_elements_by_tag_name('option')
# #
# # for option in options:
# #     if option.text == '�������':
# #         option.click()
#
# select = Select(driver.find_element_by_name('user[gender]'))
# select.select_by_value('1')
