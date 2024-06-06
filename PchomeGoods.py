# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:58:43 2022

@author: DCT
"""

import db
import datetime
import requests
import json

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"

param = {
    'q': 'nike',
    'page': '1',
    'sort': 'sale/dc'
    }

header = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'  
    }

p = input("請輸入欲搜尋的商品：")
param['q'] = p

data = requests.get(url,params=param,headers=header).text

goods = json.loads(data)

allitem = goods['prods']

for row in allitem:
    
    title = row['name']
    img = "https://cs-a.ecimg.tw" + row['picS']
    info = row['describe']
    price = row['price']
    url = "https://24h.pchome.com.tw/prod/" + row['Id']
    
    print("商品：",title)
    print("圖片：",img)
    print("簡述：",info)
    print("價格：",price)
    print("連結：",url)
    print()
    
        
    sql = "select * from products where platform='Pchome' and subject='{}'".format(title)
    
    # 建立資料庫物件集
    cursor = db.conn.cursor()
    
    cursor.execute(sql)
    
    # 筆數是0 才可以新增
    if cursor.rowcount == 0:
        today = datetime.datetime.today()
        now = today.strftime('%Y-%m-%d')
        sql = "insert into products(platform, subject, img_link, link, price, info, item) values(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, ['Pchome', title, img, url, price, info, '8'])
        """
         1家電
         2手機
         3衣服
         4電腦周邊
         5外套
         6玩具
         7公仔
         8生活用品
     """
        
        #立即提交
        db.conn.commit()

#關閉連線
db.conn.close()
        
        
        
        