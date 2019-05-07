keys = {'name', 'age', 'married', 'age'} # 不重复的
print(keys)

keys.add('test_key') # 添加
print(keys)

keys.remove('test_key') # 移除指定元素
print(keys)

keys.pop() # 随机删除
print(keys)

new_keys=keys.copy() # 拷贝
print(new_keys)

keys.clear() # 清空
print(keys)

names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}

names3 = names1.difference(names2) # 返回差集
print(names3)
print(names1)

names3 = names1.intersection(names2) # 返回交集
print(names3)

names1.difference_update(names2) # 更新为差值
print(names1)

# names1.intersection_update(names2) # 更新为交集
# print(names1)

print(names1.isdisjoint(names2)) # 是否不存在交集

print(names1.issubset(names2)) # 是否为子集

print(names1.issuperset(names2)) # 是否为超集

print(names1.symmetric_difference(names2)) # 返回对称差集

# names1.symmectric_difference_update(names2) # 更新为对称差集
# print(names1)

print(names1.union(names2))# 返回并集

names1.update(names2) # 更新为并集
print(names1)

print(names1 & names2)
print(names1 | names2)

for key in names1| names2:
    print(key)


# list / tuple / dict / set
# 类型转换？
