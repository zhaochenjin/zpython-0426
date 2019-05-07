#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/7 17:33 
# @Author   : 984185626@qq.com 
# @FileName : 7.py
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机旋转
def rndRotate():
    return random.randint(-90, 90)


# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 生成字母
def rndCharImg():
    charimage = Image.new('RGB', (60, 60), (0, 0, 0))  # 创建新的图像
    drawChar = ImageDraw.Draw(charimage)  # 创建可绘画对象
    font = ImageFont.truetype('arial.ttf', 36)  # 定义字体参数
    drawChar.text((10, 10), rndChar(), font=font, fill=rndColor2())  # 添加字母到图像中
    charimage = charimage.rotate(rndRotate())  # 旋转图像
    return charimage  # 返回生成的字母图像


# 创建主图像
width = 60 * 4  # 设置图像的宽为240
height = 60  # 设置图像的高为60
image = Image.new('RGB', (width, height), (255, 255, 255))  # 创建主图像
draw = ImageDraw.Draw(image)  # 创建可绘画对象

for x in range(width):  # 填充每个像素
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 添加模糊效果
image = image.filter(ImageFilter.BLUR)

# 添加字母到主图像中
for t in range(4):
    img = rndCharImg()
    r, g, b = img.split()  # 分离图层
    image.paste(img, (60 * t + 10, 10), r)  # 把字母图像粘贴到r图层中

# 保存图像
image.save('code.jpg', 'jpeg')
