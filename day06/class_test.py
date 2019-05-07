"""
class ClassName extends Object {
    // ...

    int i
}
"""


class ClassName(object): # 类 （object）可不写
    pass


class Human(object):

    def __init__(self, name, age, gender):  # this 强制绑定属性
        self.name = name
        self.__age = age # 私有属性
        self._gender = gender # 设为私有属性

    def fun_test(self):
        pass

    def get_name(self): # 方法
        return self.name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('Error: age < 0')

human = Human('Jerry', 18,'male') # 具体的对象

print(type(human))

human.name = 'Tom' # 自由绑定属性

print(human.name)
print(human.get_name())

tom = Human('Tom', 18, 'male')  # 具体的对象

print(tom.name)
# print(tom.__age)
# print(tom._gender)

print(tom.get_age())

# tom.set_age(-1)


# python语言自由绑定属性（一般不这样用）
tom.__age=19
print(tom.__age)  # 19

print(tom.get_age()) # 18
