def power(x): # 平方 位置参数
    return x * x


print(power(2))

def power(x, n):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2,4))

def power(x, n=3): # 默认参数
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2)) # 第二个值可能不赋值


def fn_append(array=None):
    if array is None:
        array = []
    array.append('END')
    return array


print(fn_append([1, 2, 3])) # [1, 2, 3, 'END']

print(fn_append())  # ['END']
print(fn_append())  # ['END']

print(max(1, 2, 3, 4)) # 最大值 可变参数

"""
void method(int... x)
"""

def fn_sum(*numbers): #可变参数  参数个数可变
    print(numbers)
    s = 0
    for n in numbers:
        s += n
    return s


print(fn_sum(1, 2, 3, 4, 5))
print(fn_sum())


num = (1, 2, 3, 4, 5)

print(fn_sum(num[0], num[1], num[2], num[3], num[4]))
print(fn_sum(*num))


def fn_keywords(email, password, **kw): # 关键字参数
    # print(email, password,kw)
    print(email, password)
    if 'gender' in kw:
        # todo
        pass
    if 'married' in kw:
        # todo
        pass

fn_keywords('tom@tom.com', 123, gender='male')
fn_keywords('tom@tom.com', 123, gender='male', married=False)


def fn_named_keywords(email, password, *, age, married=False, **kw): # 命名关键字参数
    print(email, password, age, married, kw)


fn_named_keywords('jerry@tom.com', 'abc', age=18)
fn_named_keywords('jerry@tom.com', 'abc', age=18, married=True)
fn_named_keywords('jerry@tom.com', 'abc', age=18, married=True, gender='male')


def fn_named_keywords(email, password, *args, age, married=False, **kw):# args 可变参数 age 命名关键字参数 married 命名关键字参数   **kw  关键字参数
    print(email, password, args, age, married, kw)
# 定义中有可变参数 可省略*
fn_named_keywords('email...', 'password...', 1, 2, 3, 'abc', age=19, gender='female')

# 参数顺序：必选参数，默认参数，可变参数，命名关键字参数，关键字参数
def fn_test(a, b=1, *c, d, **e):
    print(a, b, c, d, e)


fn_test(1, 2, 3, 4, 5,d=6)


# def fn_test(a, b=1, *c, d, **e):
#     print(a, b, c, d, e)
#
#
# c = (3, 4, 5)
#
# fn_test(1, *c, d=6)


