#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/7 2:13 
# @Author   : 984185626@qq.com 
# @FileName : collections_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 

# !/usr/bin/env python

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)
print(p.y)

print(isinstance(p, Point)) # 是否属于point
print(isinstance(p, tuple)) # 是否属于tuple

Circle = namedtuple('Circle', ['x', 'y', 'r'])

c = Circle(1, 2, 3)

print(c.x)
print(c.y)
print(c.r)

print(c._asdict())  # c 用字典表示出来

q = deque([1, 2, 3])

print(q.pop()) # 删除最右边的
print(q)
print(q.popleft()) # 删除最左边的
print(q)

q.appendleft(1) # 最左边增加1
print(q)
q.append(3) # 增加3
print(q)


def na():
    return 'N/A'


d = defaultdict(na)

# d = defaultdict(lambda: 'N/A')

d['key'] = 'value'
print(d['key']) # 输出value

print(d['k']) # 查询 K 无  返回N/A


d = dict([(1, 'x'), (2, 'y'), (3, 'z')])

print(d)

d = OrderedDict([(1, 'x'), (2, 'y'), (3, 'z')])  # 有序

print(d)

d[-1] = 'a'
d[-2] = 'b'
d[-3] = 'c'

print(d)



counter = Counter()

for c in 'programming':
    counter[c] += 1

print(counter)

words = ['hello', 'world', 'nice', 'world']

counter = defaultdict(lambda: 0) # 查询不到则返回0

for word in words:
    counter[word] += 1

print(counter)

