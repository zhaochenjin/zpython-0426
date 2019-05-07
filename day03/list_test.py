
names = ['Tom', 'Jerry']

print(names)

print(names[0])

print(names[-1])  # last element 输出最后一个
print(names[-2])  # 输出倒数第二个

print(len(names)) # 输出个数

names.append('spike') # 添加

print(names)

names.insert(2, 'Tyke') # 在2的位置添加Tyke，后面的给后面推移

print(names)

names[3] = 'Spike' # 把3的位置上的内容改为

print(names)

names.pop() # 删除最后一个

print(names)

names.pop(0) # 删除第0个

print(names)

superstars = ['Tom', 'Jerry']
names = [superstars, 'Spike'] # 嵌套
print(names[0][0])

names.clear() # 清除names

print(names)

names = superstars.copy() # 复制 superstars 的内容

print(names)

print(superstars == names)  # True

names.append('Tom') # 添加 Tom 到 names
print(names.count('Tom'))  # Tom的个数为2

superstars = ['Tom', 'Jerry']
names = ['Spike', 'Tyke']

superstars.extend(names) # 扩展
print(superstars)

print(superstars.index('Jerry')) # 返回元素索引

names.append('Spike') # 添加 Spike 到names

print(names)

names.remove('Spike') # 删除Spike 第一个指定的元素

print(names)

names.reverse() # 逆序

print(names)

names.sort(reverse=True) # 排序（正序）

print(names)

for name in names: # 迭代
    print(name)

