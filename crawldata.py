# -*- coding: UTF-8 -*-
import requests        #导入requests包
from bs4 import beautifulsoup4
url = 'https://www.zerochan.net/3012877'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)