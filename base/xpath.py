#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun

import requests
from lxml import etree

url = 'https://shanghai.zbj.com/search/f/?type=new&kw=saas'

resp = requests.get(url)

content = resp.text
# print(content)
root = etree.HTML(content)


# print(etree.tostring(root))
# /html/body/div[6]/div/div/div[2]/div[4]/div[1]/div[1]/div/div/a[1]/div[2]/div[1]/span[1]
# /html/body/div[6]/div/div/div[2]/div[4]/div[1]/div[1]/div/div/a[1]/div[2]/div[2]/p/text()
nodes = root.xpath(f'/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div')
print(len(nodes))
for node in nodes:
    print(node.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
    print(node.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()'))
    print(node.xpath("./div/div/a[1]/div[2]/div[1]/span[@class='amount']/text()"))