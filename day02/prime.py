# 判断 [101,200] 有多少个素数，并输出所有素数
# 素数：只能被 1 和它本身整除的正整数（1不是素数）

counter = 0

for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        counter = counter + 1  # ++ --

print(counter)