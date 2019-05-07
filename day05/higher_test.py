from functools import reduce


def fn_higher(f, *numbers):
    sum = 0
    for n in numbers:
        sum += f(n)
    return sum


print(fn_higher(abs, 1, 2, 3, 4, -5, -6))


def power(x, n=2):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2))

numbers = [2, 3, 4]

print(list(map(abs, numbers)))
print(list(map(power, numbers)))

print(reduce(power, numbers))
# reduce 2的3次方  为8   8的4次方
