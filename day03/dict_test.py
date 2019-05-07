d = {'name': 'Tom', 'age': 19, 'gender': 'male', 'isMarried': False}

print(d)

print(d['name'])

d = {} # 初始化

d = dict(key=123) # key =123

d['test_key'] = False # test_key = False

d = {}.fromkeys(['name', 'age'])
d = {}.fromkeys(['name', 'age'], 'value')
# {'name': 'valu12e', 'age': 'valu12e'}

print(d)

# print(d['name1']) # 查询name1 没有则报错
print(d.get('name1', 'default value'))
# 查询name1 没有则显示default value

d = {'key': 'value'} # 更新
print(d)

d['key'] = 'new value' # 更新

d['new_key'] = 'new value1' # 更新
d['new_key'] = 'new value2' # 更新

print(d)

d.update({'name':'tom'}) # 更新
d.update(age=89) # 更新
print(d)

del d['new_key'] # 删除 new_key
print(d)

d.pop('key') # 删除 key
print(d)

d.popitem() # 删除 随机删除 一般删除末尾对
print(d)

# del d #删除d
# print(d)

d.clear() #清空d
print(d)

print(len(d)) # d的长度

d_new = d.copy() # 拷贝

print(d_new)

d = {'name': 'Tom', 'age': 18, 'married': False}

print(d)

for key in d.keys():
    print(key, d[key])

for value in d.values():
    print(value)

for k, v in d.items():
    print(k,':', v)

# list1 = ['test']
# d = {list1: 'value'}
#
# print(d)
# dict 的 key 必须是不可变对象

import collections

d = collections.OrderedDict()

d = {'k1': 'v1', 'k2': 'v2'}

for key in d:
    print(key, d[key])
