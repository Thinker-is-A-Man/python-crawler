#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun
import requests

url = "https://www.sogou.com/web?query=周杰伦"
dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
resp = requests.get(url, headers=dict)

print(resp)
print(resp.text)

url = 'https://movie.douban.com/j/chart/top_list'

params = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

resp = requests.get(url, params=params, headers=headers)

print(resp.text)
print(resp.json())
resp.close()


