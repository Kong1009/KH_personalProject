# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:54:55 2022

@author: DCT
"""
import requests
from bs4 import BeautifulSoup
import db

cursor = db.conn.cursor()

for i in range(1, 10):
    url = "https://www.movieffm.net/movies/page/{}/".format(i)
    
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
    
    data = requests.get(url, headers = header).text
    
    soup = BeautifulSoup(data, 'html.parser')
    
    movies = soup.find_all('article', class_='item movies')
    
    # print(movies)
    for movie in movies:
        img = movie.find('img').get('data-lazy-src') # 圖片連結
        title = movie.find('h3').text # 標題
        date = movie.find('div', class_='data').find('span').text # 上印日期
        evaluation = movie.find('div', class_='rating').text # 評分
        evaluation = evaluation.replace(' ', '') # 評分去除空白
        link = movie.find('a').get('href') # 連結
        # area = movie.find('div', class_='metadata')
        
        sql = "select title from movies where title = '{}'".format(title)
        cursor.execute(sql)
        db.conn.commit()
        
        if cursor.rowcount == 0:
            sql = "insert into movies(title, img_link, link, evaluation, date) values('{}', '{}', '{}', '{}', '{}')".format(title, img, link, evaluation, date)
            cursor.execute(sql)
            db.conn.commit()
        
        # print('標題:{}'.format(title))
        # print('連結:{}'.format(link))
        # print('圖片:{}'.format(img))
        # print('評價:{}'.format(evaluation)) # 最高10星
        # print('日期:{}'.format(date))
        # print()
    
print('資料寫入完成')
db.conn.close()
    
    
    