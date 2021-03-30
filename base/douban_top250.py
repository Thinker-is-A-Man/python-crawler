#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun

import requests
import re
import csv

def douban_crawler(csv_writer, start):
    url = 'https://movie.douban.com/top250'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    params = {
        "start": start,
        "filter": ""
    }
    resp = requests.get(url, headers=headers, params = params)
    content = resp.text
    resp.close()

    reg = re.compile(
        "<li>.*?<em class=\"\">(?P<num>\d+)</em>.*?<span class=\"title\">(?P<title>.*?)</span>.*?<br>.*?(?P<year>\d+)&nbsp;.*?"
        "<span class=\"rating_num\" property=\"v:average\">(?P<score>.*?)</span>.*?<span>"
        "(?P<comment_count>.*?)</span>", re.S)

    iter = reg.finditer(content)

    for i in iter:
        print(i.group('num'))
        print(i.group('title'))
        print(i.group('year'))
        print(i.group('score'))
        print(i.group('comment_count'))
        dic = i.groupdict()
        csv_writer.writerow(dic.values())

f = open("/Users/liuqingyun/Desktop/豆瓣Top250.csv", mode='w')
csv_writer = csv.writer(f)
csv_writer.writerow(("排名", "电影名", "年份", "评分", "评价人数"))

for i in range(10):
    douban_crawler(csv_writer, 25*i)

f.close()