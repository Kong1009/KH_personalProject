# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:27:03 2022

@author: DCT
"""

import requests
from bs4 import BeautifulSoup
import time
import db
cursor = db.conn.cursor()
count = 0
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
for i in range(20):
    url = "https://ani.gamer.com.tw/animeList.php?page={}&c=All&sort=1".format(i)
    
    data = requests.get(url, headers = header).text
    
    soup = BeautifulSoup(data, 'html.parser')
    
    div = soup.find('div', class_='theme-list-block')
    
    all_cartoon = div.find_all('a')
    # print(all_cartoon)
    for row in all_cartoon:
        title = row.find('p', class_="theme-name").text # 標題
        link = 'https://ani.gamer.com.tw/' + row.get('href') # 連結
        year = row.find('p', class_='theme-time').text # 年分
        img = row.find('img').get('data-src') # 圖片連結
        views = row.find('p').text
        int_views = ''
        
        
        if '統計中' in views:
            int_views = 0
        
        else:
            if '.' in views:
                int_views = views.replace('萬', '000')
                int_views = int_views.replace('.', '')

            else:
                int_views = views.replace('萬', '0000')
                
        title = title.replace("'", " ")
        count += 1
        # 判斷標題是否重複
        sql = "select * from cartoons where subject = '{}'".format(title)
        cursor.execute(sql)
        db.conn.commit()
        
        
        if cursor.rowcount == 0:
            
            # 寫入資料庫
            sql = "insert into cartoons(subject, year, popularity, link, img_link, show_popularity) values('{}', '{}', '{}', '{}', '{}', '{}')".format(title, year, int_views, link, img, views)
            cursor.execute(sql)
            db.conn.commit()
        
    print("第{}頁完成".format(i+1))
    time.sleep(0.5)
    
print("資料寫入完成")
db.conn.close()
print('共{}筆'.format(count))
    # print('標題：{}'.format(title))
    # print(link)
    # print("圖片連結：{}".format(img))
    # print('年份：{}'.format(year))
    # print('總觀看數：{}'.format(views))
    
    # print()
           
    

