#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/7 1:43 
# @Author   : 984185626@qq.com 
# @FileName : datetime_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
from datetime import datetime, timedelta

print(datetime.now()) # 当前时间
print(type(datetime.now())) # 当前时间类型

now = datetime(2019, 5, 7, 11, 0, 0)
print(now)

print(now.timestamp()) # 时间戳

print(datetime.fromtimestamp(1543249292.559023)) # 时间戳变时间
print(datetime.utcfromtimestamp(1543249292.559023)) # utc时间

time = '1987-09-23 00:00:00'
print(datetime.strptime(time, '%Y-%m-%d %H:%M:%S')) # 把一个时间字符串解析为时间元组

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

print(now)
print(now - timedelta(days=1))