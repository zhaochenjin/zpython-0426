score = 70

if score > 60:
    print('pass')

if score > 60:
    print('pass')
else:
    print('failed')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')


print('x')  # 默认换行
print('x', end='\n')  # 默认换行
print('x')


# python 不换行输出 x ？

print('x', end='')
print('x', end='')

print(' ', end='')  # 1
print('x', end='')  # 2
print('x')  # 3