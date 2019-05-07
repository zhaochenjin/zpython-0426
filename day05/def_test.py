from day05.built_in_test import multi_return  # 导入函数
# 点击函数名称 ctrl + q 能看到
#
#     :param x: int...
#     :param y: float...
#     :return: tuple...

print(multi_return(1, 2)) # (1, 2)
print("...............................")

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('Error...')
#     if x > 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(-1))
# print("...............................")
#
# print(my_abs('-1'))
# print("...............................")


def fn_append(array=[]):  # default argument value is mutable
    array.append('END')
    return array


print(fn_append([1, 2, 3])) # [1, 2, 3, 'END']
print("...............................")


print(fn_append()) # ['END']
print("...............................")

print(fn_append()) # ['END', 'END']
print("...............................")