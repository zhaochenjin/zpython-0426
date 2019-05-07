# 1. 求一个数值 list 的所有元素和
A = [1, 2, 3, 4, 5]
print(sum(A))
print("............................")
# 2. 求一个数值 list 的大/小元素值
B = [1, 2, 3, 4, 5]
print(max(B))
print(min(B))
print("............................")

# 3. 求一个字符串 list 中，字符串长度大于2，且首尾字符相同的元素个数
C = ['a', 'xy', 'alabama', '101']
# print(len(C))
counter=0
for c in C:
    # print(len(c))
    # print(c)
    if (len(c) > 2) & (c[0] == c[-1]):
        # print(c)
        counter = counter + 1
    # else :
    #     print("不合格")
print(counter)
print("............................")

# 4. 把 一个 tuple 转为字符串
D =("123","1234","12345","123456")
for i in D:
    print(i)
print("............................")

# 5.对一个 tuple 进行各种切片操作
print(D[0:2])
print(D[2])
print("............................")

# 6.把 3 个 dict 合并为 1 个 dict
x = {'a':1, 'b': 2}
y = {'c': 11,'d':23}
z = {'e':111,'f':34}
w =x.update(y)
w =x.update(z)
print(x)

x = {'a':1, 'b': 2}
y = {'c': 11,'d':23}
z = {'e':111,'f':34}
w=dict(x,**y)
q =dict(w,**z)
print(q)
print("............................")

# 7. 把一个 dict 按 key 排序输出
import collections
d = collections.OrderedDict()
d = {'k1': 'v1', 'k2': 'v2'}
for key in d:
    print(key,':',d[key])
print("............................")

# 8.找出两个 dict 中的 key-value 相同项
q={'key1':1,'key2':3,'key3':2}
w={'key1':1,'key2':2}
print(q.items() & w.items()) # 找相同的键值对
print(q.keys() & w.keys()) # 找相同的键
print("............................")

# 9. 求一个 set 的大/小元素值
keys = {'1', '12', '123', '1234'}
print(max(keys))
print(min(keys))
print("............................")

# 10. 把两个 set 中的不同元素构造为一个新的 set 并输出
E = {'1', '12', '123', '1234'}
R = {'1','2','22','23','24'}
# print(E^ R)
print(E.symmetric_difference(R))
print("............................")
