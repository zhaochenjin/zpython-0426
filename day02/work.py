# 9. 一个数如果恰好等于它的因子之和，这个数就称为’完数’。例如6=1＋2＋3.编程 找出1000以内的所有完数。
for i in range(2,1001):   # 遍历1000以内的所有数，从2 开始
    s = i    # 把取出的数赋值给另一个变量s,用于与所有因子作差，若果减去所有的因子后结果为0，这个数即为完数。
    for j in range(1,i):    # 查找因子
        if i % j == 0:    # 找出因子
            s -= j      # 与因子作差
    if s == 0:     # 判断是否是完数
        print(i)     # 打印完数
print("........................")

# 10. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
sum = 0 # 起初反弹高度为0
for i in range(1,11):
    print(100/(2 ** i))  # 输出十次的高度
    h = 100/(2 ** i) # 每次的高度
    sum = sum + h
print(sum)
print("........................")

# 13. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if (i+100)==j*j and (i+268)==k*k:
                print(i)

import math
for z in range(10000):
    x=int(math.sqrt(100+z))
    y=int(math.sqrt(268+z))
    if (x*x==(100+z))and (y*y==(z+268)):
        print (z)
print("........................")

# 14. 输入某年某月某日，判断这一天是这一年的第几天？(闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为 闰年。)
import datetime

y = int(input('请输入4位数字的年份：'))  # 获取年份
m = int(input('请输入月份：'))  # 获取月份
d = int(input('请输入是哪一天：'))  # 获取“日”

targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期
print(targetDay - datetime.date(targetDay.year - 1, 12, 31))  # 减去上一年最后一天，可得解
print("........................")

# 15. 输入三个整数x，y，z，请把这三个数由小到大输出。
numbers = []
for i in range(1,4):
       x = int(input(f"请输入第{i}个整数："))
       numbers.append(x)
print(f"未排序之前是：{numbers}")
print("由小到大排序完后是：",sorted(numbers))
print("........................")

# 16. 输出9*9口诀
for i in range(1,10):
 for j in range(1,i+1):
  print(j,'*',i,'=',i * j ,end=" ")
 print(' ')
print("........................")

# 19.菱形
for i in range(1, 5):
    for j in range(4 - i, 0, -1):
        print(' ', end='')
    for k in range(0, (i - 1) * 2):
        print('x', end='')
    print('x')
for i in range(1, 4):
    for j in range(0, i):
        print(' ', end='')
    for k in range(4, (i - 1) * 2, -1):
        print('x', end='')
    print('x')
print("........................")

# 20. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
a = 2
b = 1
sum=0
for i in range(1,21):
    a=a+b
    b=a-b
    sum=sum+a/b
print(sum)
print("........................")

# 21.求1+2!+3!+…+20!的和。
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print(s)
print("........................")

# 22.利用递归方法求5!。
def fact(i):
 sum = 0
 if i == 0:
  sum = 1
 else:
  sum = i * fact(i - 1)
 return sum
print(fact(5))
print("........................")

# 53.请根据 BMI 公式，根据用户输入计算 BMI 指数，并输出测试结果
x = input('请输入weight（kg)：')
y = input('请输入height(m)：')
bmi=float(float(x)/float(y)/float(y))
# print(bmi)
if bmi <=18 :
    print("过轻")
elif bmi <=25 :
    print("正常")
elif bmi <=28 :
    print("过重")
elif bmi <= 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")
print("........................")
