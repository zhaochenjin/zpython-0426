class Human(object):
    def __init__(self, name):
        self.name = name

    def study(self): # 方法
        print('human studying...')


class Chinese(Human): # 继承

    def study(self): # Ctrl+ O 重写父类的方法
        # super().study()
        print('Chinese studying...')

zhangsan = Chinese('Zhang san') # 子类实例

zhangsan.study()

print(zhangsan.name)

print(isinstance(zhangsan, Chinese)) # zhangsan 是不是Chinese的实例
print(isinstance(zhangsan, Human)) # zhangsan 是不是Human的实例


def fn_study(human):
    human.study()


fn_study(zhangsan)


class Duck(object):

    def study(self):
        print('Duck can study?')


yellow = Duck()

fn_study(yellow)

print(type(abs))
print(type(fn_study))


print(dir(zhangsan))# 获取内置属性

print(zhangsan.__class__) # 属于什么类型

print(dir('abc')) # 字符串类型所有属性和方法

print(len('abc')) # 字符的个数
print('abc'.__len__())

