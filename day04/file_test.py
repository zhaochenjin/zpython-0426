import os
import shutil

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('not exits.')
    # 如果存在 则删除 否则输出不存在

os.rename('download.py', 'download_test.py') # 把download.py改名为download_test.py

shutil.copy('file_test.py', 'file_test_new.py') # 复制file_test.py 并取名为file_test_new.py

# split ext:extension 扩展名
print([x for x in os.listdir('.') if os.path.isfile(x)])  # 列表生成器
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])  # 列表生成器

print(os.path.splitext('file_test.py')) # 将文件名和扩展名分开
