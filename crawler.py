#!usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

print("开始执行")
resp = requests.get('http://amr.gd.gov.cn/zwgk/tzgg/content/post_3178563.html')
resp.encoding = 'utf-8'
content = resp.text
bs = BeautifulSoup(content,'html.parser')
title = bs.select("title")
print("文章名称是：")
print(title[0].get_text())
page_date = bs.find(attrs={"name": "PubDate"})['content']
print("文章发布的时间是：")
print(page_date)
print("数据已经成功记录！")
