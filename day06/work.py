# 1. 定义类，实现power（x,y)功能
class Solution:
    def power(self, a, b):
        # self.a=a
        # self.b=b
        return a ** b


print(Solution().power(2, -3))
print(Solution().power(3, 5))
print(Solution().power(100, 0))
print("..............................")


# 2. 定义类，实现字符串逆序
# class Solution:
#     def reverse_words(self):
#         return self[::-1]
#     print(reverse_words('hello.py'))

class Solution:
    def reverse_words(strDemo):
        strList = list(strDemo)
        strList.reverse()
        return ''.join(strList)

    print(reverse_words('hello.py'))


print("..............................")


# 3. 定义三角形类，实现求三角形周长和面积的方法，属性为三个边长
class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if self.a + self.b < self.c:
            print("无法构成三角形")
        elif self.b + self.c < self.a:
            print("无法构成三角形")
        elif self.a + self.c < self.b:
            print("无法构成三角形")
        else:
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


rectangle = Rectangle(1, 1, 3)
# rectangle=Rectangle(3,4,5)
print(rectangle.perimeter())
print(rectangle.area())
print("..............................")


# 4. 定义立方体类，属性为长度、宽度、高度，通过方法来计算它的体积
class Cube:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


cube = Cube(2, 3, 4)
print(cube.volume())
print("..............................")


# 5.定义一个人类，包含姓名、性别、年龄等信息 所有的变量必须私有。
# 其他类只能通过该类的方法获取和修改
# 实例化一个人类，试着通过该类的方法修改实例化的人的信息
class Human:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__sex

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, sex):
        self.__sex = sex

    def set_age(self, age):
        self.__age = age


human = Human("zhao", "nan", 23)
print(human.get_age())

human.set_age(98)
print(human.get_age())
print("..............................")


# 6.定义一个学生类，包含三个属性（学号，姓名，成绩）均为私有的
# 分别给这三个属性定义两个方法，一个设置它的值，另一个获得它的值
# 测试这些方法
class Student:
    def __init__(self, num, name, grade):
        self.__num = num
        self.__name = name
        self.__grade = grade

    def get_num(self):
        return self.__num

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def set_num(self, num):
        self.__num = num

    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

student = Student(1980765, "zhao", 96)
print(student.get_num())

student.set_num("1860510807")
print(student.get_num())
print("..............................")


# 7.继承人类编写一个学生类，为学生类添加新的属性和方法，并进行测试
class Students(Human):
    def __init__(self, name,sex,age,num,grade):
        Human.__init__(self,name,sex,age)
        self.__num = num
        self.__grade = grade

    def get_num(self):
        return self.__num

    def get_grade(self):
        return self.__grade

    def set_num(self, num):
        self.__num = num

    def set_grade(self, grade):
        self.__grade = grade

    def study(self):
        return("个人信息已输出")
students = Students("zhao", "nan",18,1850510301,92,)
print(students.get_name())
print(students.get_age())
print(students.get_num())
print(students.study())