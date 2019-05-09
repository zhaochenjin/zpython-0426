#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/9 17:07 
# @Author   : 984185626@qq.com 
# @FileName : select_test.py 
# @GitHub   : https://github.com/zhaochenjin/zpython-0426 
 
import mysql.connector

connection=mysql.connector.connect(user='root',password='123456')

connection.autocommit = True  # 自动提交

cursor=connection.cursor()

cursor.execute('select * from db_python.user')

records=cursor.fetchall() # 接收全部的返回结果行

print(records)
#
for recond in records:
    print(recond)



# 查询
cursor.execute("""
    select * from db_python.book
    where id > 3
    order by id desc
    limit 0, 2  # 只读取2个
""")

rows = cursor.fetchall()

for row in rows:
    print(row)



# 更新
cursor.execute("""
    update db_python.book
    set title = 'JavaScript 高级编程'
    where title = 'JavaScript'
""")

connection.commit()  # 提交事务



# 查询
cursor.execute("""
    select u.email , b.title
    from db_python.user u join db_python.book b
    on u.id = b.userId
""")

values = cursor.fetchall()

for value in values:
    print(value)



# 删除外键
cursor.execute('alter table db_python.book drop foreign key book_fk_userId')

# 重建外键约束
cursor.execute("""
    alter table db_python.book
    add constraint
    book_fk_userId
    foreign key (userId)
    references db_python.user(id)
    on delete set null
""")

cursor.execute("""
    delete from db_python.user
    where id = 1
""")

cursor.execute('drop table db_python.book') # 先删除从表
cursor.execute('drop table db_python.user') # 再删除主表
