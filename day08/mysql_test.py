# 安装sql.connector包
#  activate zpython-0426  激活项目
#  conda install mysql-connector-python


#!/usr/bin/env python # -*- coding: UTF-8 -*-

# @Time     : 2019/5/8 10:47 
# @Author   : 984185626@qq.com 
# @FileName : mysql_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='123456'
)



cursor = connection.cursor()

cursor.execute('drop database if exists db_python')
cursor.execute('create database db_python')  # 增数据库
cursor.execute('show databases') # 展示数据库

for db in cursor: # 查询所有的数据库
    print(db)



cursor.execute('drop table if exists db_python.user')

sql = """
create table db_python.user(
    id int auto_increment primary key comment 'id PK',
    email varchar(255) not null unique comment 'email NN UN',
    password varchar(255) not null comment 'password NN'
)comment 'user table';
"""

cursor.execute(sql)



cursor.execute('drop table if exists db_python.book')

sql = """
create table db_python.book(
    id int auto_increment primary key comment 'id PK',
    title varchar(255) not null unique comment 'title NN UN',
    author varchar(255) not null comment 'password NN',
    userId int comment 'user id FK'
)comment 'user table';
"""

cursor.execute(sql)



cursor.execute(""" # user表  book表  外键关系
alter table db_python.book
add constraint book_fk_userId
foreign key(userId)
references db_python.user(id)
""")



cursor.execute('show tables from db_python')

for table in cursor: # 展示两个表
    print(table)



cursor.execute("""
insert into db_python.user(email, password) # 增
value ('tom@tom.com', '123'),('jerry@tom.com', 'abc')
""")
print(cursor.rowcount)  # 2

sql = 'insert into db_python.user(email, password) value (%s, %s)'
val = ('spike@tom.com', '456')

cursor.execute(sql, val)

connection.commit() # 提交事务

print(cursor.rowcount)



cursor.execute('''
insert into db_python.book(title, author, userId) # 增
values
('HTML','author-1', 1),
('CSS','author-2', 2),
('JavaScript','author-3', 2),
('MyBatis','author-4', 3),
('Spring','author-5', 3),
('Python 编程基础','author-6', 3)
''')
print(cursor.rowcount)

connection.commit() # 提交事务



