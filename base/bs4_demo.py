#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun

import requests
from bs4 import BeautifulSoup
import os

# os.mkdir("/Users/liuqingyun/Desktop/爬虫壁纸")

p_url = 'https://www.umei.cc/bizhitupian/'
p_resp = requests.get(p_url)
p_resp.encoding = 'utf-8'

page = BeautifulSoup(p_resp.text, features='html.parser')
# print(page)

alist = page.find("div", attrs={"class": "TypeList"}).findAll("a")

for i in alist:
    c_url = i.get("href")
    print(i.get("href"))
    c_resp = requests.get(c_url)
    c_resp.encoding = "utf-8"
    c_page = BeautifulSoup(c_resp.text, "html.parser")

    img = c_page.find("div", attrs={"class": "ImageBody"}).find("img")
    img_src = img.get("src")
    img_name = img.get('alt') + img_src.split("/")[-1]
    img_resp = requests.get(img_src)
    img_resp.close()
    with open(f"/Users/liuqingyun/Desktop/爬虫壁纸/{img_name}", mode='wb') as f :
        f.write(img_resp.content)

