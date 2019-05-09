#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/8 9:00 
# @Author   : 984185626@qq.com 
# @FileName : sqlite_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 


import sqlite3

connection = sqlite3.connect('test.db') # 创建数据库

# print(connection)
# print(type(connection))

cursor = connection.cursor()  # 获取cursor  使用该连接创建并返回游标

cursor.execute('drop table if exists user')
cursor.execute( '''
                create table if not exists user(
                        id int primary  key,
                        name varchar(20)
                        ) ''')



cursor.execute("insert into user(id, name) values(1, 'Tom')")   #增
cursor.execute("insert into user(id, name) values(2, 'Jerry')")  # 增
cursor.execute("insert into user(id, name) values(3, 'zhao')")  # 增

connection.commit() # 提交事务

print(cursor.rowcount) #结果行数

values = cursor.fetchall() # 接收全部的返回结果行
print(values)
print(".............................")


# cursor.execute('select * from user where id = ?', (1,)) # 查
cursor.execute('select * from user') # 查

print(cursor.rowcount) #结果行数

values = cursor.fetchall() # 接收全部的返回结果行
print(values)
print(".............................")



cursor.execute('update user set name = ? where id = ?', ('jerry', 1)) # 更新

cursor.execute('select * from user where id = ?', (1,))

connection.commit() # 提交事务

print(cursor.rowcount) #结果行数

values = cursor.fetchall()
print(values)
print(".............................")



cursor.execute('delete from user where id = ?', (1,)) # 删除

cursor.execute('select * from user where id = ?', (1,))

connection.commit() # 提交事务

print(cursor.rowcount) #结果行数

values = cursor.fetchall()
print(values)



cursor.close()
connection.close()