#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun
import requests

url = 'https://fanyi.baidu.com/sug'

kw = input('请输入：')

data = {
    'kw': kw
}
resp = requests.post(url, data=data)

# print(resp.text)
print(resp.json())
resp.close()