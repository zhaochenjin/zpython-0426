import os
import platform

print(os.name)  # D:/data 获取当前的系统类型

# print(os.uname())
print(platform.uname())
print("..................")

print(os.environ)
print("..................")

print(os.environ.get('PATH'))
print("..................")
