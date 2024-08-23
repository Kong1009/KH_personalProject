# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:46:13 2022

@author: DCT
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.sum.com.tw/carsearch.php?v=4&brand=&model=&price1=&price2=&year1=&year2=&q=&cc1=&cc2=&price_rang=&exhaust="


data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

# ul = soup.find('ul', class_='carWrap boxWrap')

car_list = soup.find_all('div', class_='shop-list')
for row in car_list:
    car_park = row.find('a', class_='subj').text
    car_name = row.find('div', class_='titleDetail').find('span', class_='model').text
    displacement = row.find('dd', class_='focusInfo').text
    
    displacement = displacement.replace('\n', '')
    displacement = displacement.split['.']
    
    price = row.find('div', class_='price').text
    # mileage = row.find('dd', class_='focusInfo')[2].text
    # 
    print(car_park)
    print(car_name)
    print(displacement[0])
    print(displacement[1])
    # print(price)
    print()

# print(car_list)

