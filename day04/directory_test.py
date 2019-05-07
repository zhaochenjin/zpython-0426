import os

print(os.path.abspath('.')) # 绝对路径

print(os.getcwd()) #获取当前的路径

print(os.path.join('d:/test1', 'test2', 'test.txt')) #连接路径名组件

# print(os.makedirs(os.path.join('.', 'new_dir', 'sub_dir')))
# 创建多级目录  创建new_dir 在给里面创建sub_dir

# print(os.rmdir(os.path.join('.', 'new_dir')))
# 创建单个目录

print(os.path.split('new_dir/sub_dir/test.txt')) # 返回路径的目录名和文件名

print(os.path.splitext('google.com.png')) # 分离扩展名

print([x for x in os.listdir('.') if os.path.isdir(x)]) # 输出目录
