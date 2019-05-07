names = ('Tom', 'Jerry')

print(names)

numbers = (1,) # tuple中只有一个的写法

print(numbers)  # (1)

print(names[-1]) # 输出最后一个

print(1 in numbers) # 包含

print(2 not in numbers) # 不包含

print(len(names)) # 个数

names = tuple(('test', 'test'))

print(names)

print(names.count('test')) # 名字为test的个数为2

print(names.index('test')) # 索引 第一个出现test的位置

superstars = ['Tom', 'Jerry']
names = (superstars, 'Spike')

print(names)

names[0].append('Tester')

print(names)

for name in names:
    print(name)

