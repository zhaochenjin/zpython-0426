with open('test.txt', 'w') as f: # 原来写的都消失了   w write 写
    f.write("你好hello1")
with open('test.txt', 'a') as f:  #  a append 追加
    f.write("你好hello2")


# with open('test_new.txt', 'x') as f:  # x create 创建
#     f.write("你好hello2")


with open('1.jpg', 'rb') as f1:
    with open('2.jpg', 'wb') as f2:
        f2.write(f1.read())

