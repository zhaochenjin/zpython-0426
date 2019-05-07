import os

from urllib.request import urlopen

f = open('D:/zpython.txt','rt', encoding='utf-8')
print(f.read())
f.close()

with open('d:/zpython.txt', encoding='utf-8') as f:
    print(f.read())

with open('d:/zpython.txt', encoding='utf-8') as f:
    print(f.read(3))  # 只输出三个字符 英文三个字母 汉字三个
    # pass # 不做任何处理

print("······················")

with open('d:/zpython.txt', encoding='utf-8') as f:
    pass
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
print("······················")

s = ' Hello, World! '
print(s.strip()) # 输出 把空字符删掉
print(s.lstrip())  # l:left 把左边的空字符删掉
print(s.rstrip())  # r:right 把右边的空字符删掉

with open('d:/zpython.txt', encoding='utf-8') as f:
    for x in f:
        print(x.strip())

with open('d:/zpython.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())

# with open('1.jpg', 'rb') as f:
#     print(f.read())
    #  pass

print(os.getcwd())  # current working directory 输出所在位置

with urlopen('https://book.douban.com/subject/1005022/') as f: # 读取页面信息
    for line in f.readlines():
        print(line.decode('UTF-8').strip())

with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4') as f:
    for line in f.readlines():
        line = line.decode('utf-8')
        if 'img class=""' in line:
            print(line.strip()[len('<img class="" src="'):len(line.strip())-1]) # 切片 从<img class="" src=" 开始