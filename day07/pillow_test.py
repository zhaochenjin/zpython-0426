#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/7 15:41 
# @Author   : 984185626@qq.com 
# @FileName : pillow_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
from PIL import Image, ImageFilter

image = Image.open('pillow.jpg')
w, h = image.size
image.thumbnail((w//2, h//2))
image.save('new.jpg') # 另存为new.jpg

image = Image.open('pillow.jpg')
image_blur = image.filter(ImageFilter.BLUR) # 照片变模糊
image_blur.save('blur.jpg')