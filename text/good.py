#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/9 10:35 
# @Author   : 984185626@qq.com 
# @FileName : good.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 

import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='123456'
)


cursor = connection.cursor()

cursor.execute('drop database if exists db_goods')
cursor.execute('create database db_goods')  # 创建数据库
cursor.execute('show databases') # 展示数据库

for db in cursor: # 查询所有的数据库
    print(db)
print(".................................")


cursor.execute('drop table if exists db_goods.good') # 新建商品表

sql = """
create table db_goods.good(
    id int auto_increment primary key comment 'id PK',
    num int(255) not null unique comment '商品编号',
    name varchar(255) not null comment '商品名称',
    price int(255) comment '单价',
    number int(255) comment '数量'
)comment 'db_goods good';
"""

cursor.execute(sql)

cursor.execute('show tables from db_goods') # 查询所有表查看是否新建成功
for table in cursor:
    print(table)
print(".................................")



# 商品的新增
cursor.execute("""
insert into db_goods.good(num,name,price,number)
value ('1111','Apple','10','100'),('1112','Banana','8','120'),('1113','Melon','20','50')
""")
print(cursor.rowcount)

sql = 'insert into db_goods.good(num,name,price,number) value (%s, %s, %s, %s)'
val = ('1114','grapy','15','30')

cursor.execute(sql, val)

connection.commit() # 提交事务

print(cursor.rowcount)
print(".................................")



# 商品的展示
cursor.execute('select * from db_goods.good')

print(cursor.rowcount) #结果行数

values = cursor.fetchall() # 接收全部的返回结果行
print(values)
print(".................................")



# 按照名字查询
cursor.execute("""select * from db_goods.good where name ='Apple'""")

print(cursor.rowcount) #结果行数

values = cursor.fetchall() # 接收全部的返回结果行
print(values)
print(".................................")



# 更新
cursor.execute("""update db_goods.good set name ='apple' where id = 1""")

connection.commit() # 提交事务

print(cursor.rowcount) #结果行数
