#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/7 1:41 
# @Author   : 984185626@qq.com 
# @FileName : base64_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
import base64

s = b'Hello, World!'

print(base64.encodebytes(s)) # 加密

print(base64.decodebytes(b'SGVsbG8sIFdvcmxkIQ==\n')) # 解密