# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:34:47 2022

@author: DCT
"""

import db
import datetime
import requests
from bs4 import BeautifulSoup

url = "https://tw.buy.yahoo.com/search/product"

data = {}

product = input("請輸入欲查詢的產品：")

data['p'] = product

#requests 帶參數，參數需要用字典方式傳送

content = requests.get(url,params=data).text

soup = BeautifulSoup(content,'html.parser')

allgoods = soup.find('div',class_='ResultList_resultList_IpWJt')

goods = allgoods.find_all('a', class_='sc-dwnOUR ixMORF')

# print(goods)
for row in goods:
    title = row.find('span',class_='sc-AHaJN sc-gScZFl sc-jNJNQp gjfZOz hAUjCv bkSrYN').text
    price = row.find('span', class_='sc-AHaJN sc-gScZFl JwHYQ kpwUrI').text
    
    price = price.replace('$','')
    price = price.replace(',','')
    

    
    link = row.get('href')

    # print("商品：",title)
    # print("價格：",price)
    
    # print("超連結：",link)
    
    
    shop_url = link
    shop_content = requests.get(shop_url,params=data).text

    shopsoup = BeautifulSoup(shop_content,'html.parser')
    # imgcontent = shopsoup.find('div', class_='LensImage__imgWrapper___SXnau')
    imgcontent = shopsoup.find('div', class_='LensImage__container___3jpgS')
    # print(imgcontent)
    # print()
    try:
        img = imgcontent.find('img').get('src')
        # print(img)
        # print()
    except:
        continue


    
    #
    sql = "select * from products where platform='Yahoo' and subject='{}'".format(title)
    
    # 建立資料庫物件集
    cursor = db.conn.cursor()
    
    cursor.execute(sql)
    
    # 筆數是0 才可以新增
    if cursor.rowcount == 0:
        today = datetime.datetime.today()
        now = today.strftime('%Y-%m-%d')
        sql = "insert into products(platform, subject, img_link, link, price,  item) values(%s, %s, %s, %s, %s,  %s)"
        cursor.execute(sql, ['Yahoo', title, img, link, price, '8'])
        
         # 1家電
         # 2手機
         # 3衣服
         # 4電腦周邊
         # 5外套
         # 6玩具
         # 7公仔
         # 8生活用品
         
        #立即提交
        db.conn.commit()

#關閉連線
db.conn.close()
print('OK完成')