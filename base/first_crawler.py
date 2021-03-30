#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author:  liuqingyun

from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)

with open("../html/baidu.html", mode="w") as f:
    f.write(resp.read().decode('utf-8'))