print(dir('__builtins__')) # 内置函数

print(abs(-1)) # 绝对值

print(max(1, 2)) # 最大值

print(min(-1, 0, 1, 2)) # 最小值

# n = int(input()) # 类型转换
#
# print(n + 1)
#
# n = float(input()) # 类型转换
#
# print(n + 1)

print(str(123) + 'test')

a = [1, 2, 3, 1, 2, 3]  # a list

b = tuple(a) # b tuple

print(b)

c = set(a)  # c set  去掉重复的值

print(c)

d = set(b)

print(c, d) # {1, 2, 3} {1, 2, 3}

print(type(a), type(b), type(c), type(d))

absolute = abs # 函数别名

print(absolute(-1))


def add(x, y):
    return x + y


print(add(1, 2))


def test():
    pass
    # return


print(test()) # None

def multi_return(x, y):
    """
    :param x: int...
    :param y: float...
    :return: tuple...
    """
    return x, y


m, n = multi_return(1, 2)

print(m, n) # 1 2

print(multi_return(3, 4)) # (3, 4)
