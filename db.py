# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:24:42 2022

@author: DCT
"""

import pymysql 

dbsetting = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456789",
    "db": "myweb",
    # "db": "testweb",
    "charset": "utf8"
    }

conn = pymysql.connect(**dbsetting)