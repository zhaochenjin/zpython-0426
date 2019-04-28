# 打印出 n 行图案（菱形）

n = input()

#9.
counter = 0

for i in range(3, 1000):
    for j in range(1, i):
        if i % j == 0:
            i -=j
    if i == 0:
        print(i)
        counter = counter + 1  # ++ --

print(counter)

