import math

print(math.pi)

class Circle():

    pi=3.14

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


    def area(self):
        return self.r * self.r * math.pi

c = Circle(1, 2, 3)
print(c.pi)
print(Circle.pi)
c2=Circle(4,5,6)

print(hasattr(c, 'x')) # c 里面是否有x
print(hasattr(c, 'y')) # c 里面是否有x

print(getattr(c, 'x')) # 返回对象属性值
print(getattr(c, 'y')) # 返回对象属性值


print(getattr(c, 'z', 'not found')) # 没有的话返回not found

setattr(c,'z',4) # 把4 给 z 的属性值
print(getattr(c,'z')) # 返回 z 的属性值 4

print(hasattr(c,'area')) # c 里面是否有 area

print(getattr(c, 'area')) # 返回 area 的属性值

fn = getattr(c, 'area')

fn()

print(fn()) # 圆形面积

c.pi=4
print(c.pi)
print(Circle.pi)