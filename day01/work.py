# 1.
print("""
    登 鹳 雀 楼
    - 【唐】王之涣

    白日依山尽，
    黄河入海流。
    欲穷千里目，
    更上一层楼。
""")

# 2.
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# 3
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

#4.
import math
radius=float(input("请输入半径："))
area=math.pi* radius * radius
print ( "圆的面积为: %.2f"% area)

#5.
'''
num = "1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # True
num.isdecimal() # False
num.isnumeric() # True

num = "四" # 汉字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # True


isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''


