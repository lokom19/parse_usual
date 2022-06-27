# -*- coding: utf-8 -*-

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r'C:\projects\requests\geckodriver.exe', options=options)

orders = []
locations = []
times = []
users = []
prices = []
descriptions = []
titles = []
categories = []

pages = 5

for j in range(1, pages):
    time.sleep(2)
    for i in range(1, 21):
        # try:

        driver.get(f'https://www.remontnik.ru/boards/kamchatskiy_kray/?page={j}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        elementt0 = soup.find_all('div', class_='title')
        print(elementt0[i-1].text)
        titles.append(elementt0[i-1].text)
        time.sleep(5)
        element = driver.find_element_by_xpath(
            f'/html/body/div[2]/div[3]/div/div[3]/div[1]/div[{i}]/div[1]/div/a')
        element.click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        elementt = soup.find('li', class_='order')
        try:
            orders.append(elementt.text)
            print(elementt.text)
        except:
            orders.append('-')
        elementt2 = soup.find('li', class_='location')
        locations.append(elementt2.text)
        print(elementt2.text)
        elementt3 = soup.find('li', class_='time')
        times.append(elementt3.text)
        print(elementt3.text)
        elementt4 = soup.find('li', class_='user').find('a', href=True)
        users.append(elementt4.text)
        print(elementt4.text)
        elementt5 = soup.find('span', class_='lowercase')
        prices.append(elementt5.text)
        print(elementt5.text.encode())
        elementt6 = soup.find('div', class_='order-details')
        descriptions.append(elementt6.text)
        print(elementt6.text)
        elementt7 = soup.find('div', class_='order__categories').find('a', href=True)
        categories.append(elementt7.text)
        print(elementt7.text)


import pandas as pd
df = pd.DataFrame({'Заказ':[i for i in titles], 'Номер': [i for i in orders], 'Место': [i for i in locations], 'Дата': [i for i in times],
                   'Заказчик': [i for i in users], 'Цена': [i for i in prices], 'Описание': [i for i in descriptions], 'Категория': [i for i in categories]})
print(df)
df.to_excel(r'C:\Users\lokom\OneDrive\Рабочий стол\kamchatka.xlsx', index=False)