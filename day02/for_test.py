for i in range(0, 10, 2):
    print(i)

fruits = ['apple', 'banana', 'orange']  # list 列表
for fruit in fruits:
    print(fruit)
else:  # 循环正常结束后的处理：没有 break
    print('else...')
# 输出apple banana orange 输出else...

fruits = []  # list 列表
for fruit in fruits:
    print(fruit)
else:  # 循环正常结束后的处理：没有 break
    print('else...')
# 只输出else...

fruits = ['apple', 'banana', 'orange']  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        print('found watermelon.')
        break
else:  # 循环正常结束后的处理：没有 break
    print('not found watermelon.')
# 输出apple banana orange not found watermelon.

fruits = ['apple', 'banana', 'orange']  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
else:  # 循环正常结束后的处理：没有 break
    print('else...')
# 输出 apple banana

print("-------------------------------")
is_found = False
fruits = ['apple', 'banana', 'orange']  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        print('found watermelon.')
        is_found = True
        break
if not is_found:
    print('not found watermelon.')

# 语法糖 syntactic sugar: 在没有改变语言功能的前提下，是程序的写法更加简洁
# 语法： 盐/糖精/海洛因

# 2: for-else


