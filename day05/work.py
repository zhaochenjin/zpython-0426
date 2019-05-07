from functools import reduce
# 1.定义函数，统计一个字符串中大写，小写字母的个数
# a=input("请输入字符串：")
# counterd=0
# counterx=0
# for i in range(65,123):
#     if a.count(chr(i))==0:
#         continue
#     elif 'A'<= (chr(i))<= 'Z' :
#         print(chr(i), ":", a.count(chr(i)))
#         counterd=counterd+1
#     else:
#         print(chr(i),":",a.count(chr(i)))
#         counterx=counterx+1
# print("大写字母有",counterd,"个")
# print("小写字母有",counterx,"个")

def count(str):
    char_number1 = char_number2  = 0
    for char in str:
        if char.isupper():
            char_number1 =char_number1+1
        else :
            char_number2 = char_number2+1
    print("大写字母个数：",char_number1)
    print("小写字母个数：",char_number2)
    return


count("qwAZV")

# 2. 定义函数，把一个list的元素去重，返回新list
def delList(L):
         L1 = []
         for i in L:
             if i not in L1:
                 L1.append(i)
         print(L1)
         return L1


delList([3, 2, 2, 4, 6, 5, 1])

# 3.裴波那契数列第n项Fibonacci sequence
# 0,1,1,2,3,5,8,13,21,34,...
def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(5))

# 4. 汉诺塔N圆盘移动步骤 Tower of Hanoi
# n = 2
# A - B
# A - C
# B - C

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)   #将过渡位


move(2,'A','B','C')

# 5. 打印杨辉三角
#       １
#       １１
#        １２１  
#       １３３１   
#      １４６４１
#   １５ 10 10 ５１
#   １6 15 20 15 ６１  
#   1 7 21 35 35 21７１
# １８ 28 56 70 56 28 8 1     

def yanghui(t):
    print([1])
    line=[1,1]
    print(line)
    for i in range(2,t):
        r=[]
        for i in range(0,len(line)-1):
            r.append(line[i]+line[i+1])
        line=[1]+r+[1]
        print(line)
yanghui(8)

# 6. 参数组合练习
def fn_test(a, b=1, *c, d, **e):
    #  必选参数，默认参数，可变参数，命名关键字参数，关键字参数
    print(a, b, c, d, e)


fn_test(1, 2, 3, d=4)

# 7.高阶函数 map/reduce/filter/sorted 练习
def add(x,y=1):
    p=x+y
    return p
num=[2,5,8]
print(list(map(add,num)))
print(reduce(add, num))

def add(x,y=1):
    p=x+y
    return p<5
num=[2,5,8]
print(list(filter(add,num)))


print(list(sorted([1,2,-100,-4],key=abs)))
# 按数字绝对值大小比