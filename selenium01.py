from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
# import db
import time

options = webdriver.ChromeOptions()

prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
    
options.add_experimental_option('prefs',prefs)


path = "C:/Comprehensive_Web/chromedriver.exe"

driver = webdriver.Chrome(path, chrome_options = options)


driver.get('https://shopping.pchome.com.tw/')

search = driver.find_element_by_class_name("c-siteSearchInput")

# s = input("搜尋類別：")
# search.send_keys(s)

search.send_keys('3C')

search.send_keys(Keys.RETURN)


# for i in range(5):
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "prod_img"))
    )


# url = (driver.current_url)

# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

# data = requests.get(url, headers = header).text

# soup = BeautifulSoup(data, 'html.parser')
# print(soup)


# 捲動視窗並等待瀏覽器載入更多內容


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 捲動視窗到底部
time.sleep(2)


title = driver.find_elements_by_class_name("prod_name") # 標題
link = driver.find_elements_by_css_selector("h5.prod_name > a") # 連結
img = driver.find_elements_by_tag_name("a.prod_img > img") # 圖片
price = driver.find_elements_by_class_name("price")
    

tt = []
pr = []
for t, l, i, p in zip(title, link, img, price):
    
    print('標題：',t.text)
    print('連結：',l.get_attribute('href'))
    print('圖片：',i.get_attribute('src'))
    print('價格：',p.text.replace('$', ''))
    print()
    tt.append(t.text)
    pr.append(p.text)
    
print(len(tt))
print(len(pr))



        

print(driver.current_url)
driver.quit()