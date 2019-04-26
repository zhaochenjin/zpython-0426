s = 'Hello, World!'

s = 'hello, World!'



print(s[0])
# h

print(s * 3)
# hello, World!hello, World!hello, World!

print(s[4:8])
# o, W     4到7

print('He' in s)
# False

print('H' not in s)
# True

print(s.capitalize())
# Hello, world!    大写

print(s.center(20, '-'))
# ---hello, World!----

print(s.zfill(20)) #  zero fill
# 0000000hello, World!

print(s.count('l'))
# 3  l的个数

print(s.endswith('!', 0, 1))
# False   0开头 1结尾 是否以！结尾

print(s.endswith('!', 0, 13))
# True  0开头 13结尾 是否以！结尾

print(s.find(',', 10, 13))
# -1 查找不到返回-1

s = 'hello, World!'
print(s.find('d', 10, 13))
# 11 返回子字符串第一个匹配项出现在字符串中的索引位置
