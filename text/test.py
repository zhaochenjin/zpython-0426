import sys

import numpy as np
import re
from tkinter import Tk, Button, filedialog, ttk, S, E, W, N, Frame, Label, Text, TOP, BOTH
from urllib.request import urlopen

from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from wordcloud import WordCloud
import jieba
from scipy.misc import imread
from os import path
from PIL import Image

import mysql.connector




class Test_Work():

    def __init__(self):
        self.initSQL()
        self.querySQL_result = []
        self.mysqlcursor
        self.sql_to_execute = ''
        self.init()

        pass

    def initSQL(self):
        mysqldb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            database='jdbcStudy'
        )
        self.mysqlcursor = mysqldb.cursor()
        # mysqlcursor.execute(sql)
        # print('mysqlsursor ' + mysqlcursor)
        # for x in mysqlcursor:


    def executeSQL(self):
        self.mysqlcursor.execute(self.sql_to_execute)
        for x in self.mysqlcursor:
            print(x)
            self.querySQL_result.append(str(x))



    def init(self):
        todo = input('''hello, Welcome to product system:
        what do u wanna to do?(Please input num and press enter)
        1 : query what and how many products stored now in system
        2 : add new product
        3 : edit product information
        4 : quit
        ''')
        if  todo == 1:
            self.query_product()
        elif todo == 2:
            self.add_new_product()
        elif todo == 3:
            self.edit_product_info()
        else:
            sys.exit()

    def query_product(self):
        self.sql_to_execute = 'select * from productForTest;'
        print('This is specified info about what u stored:')
        self.executeSQL()
        for x in self.querySQL_result:
            print(x)
        print("that all!")
        self.init()



    def add_new_product(self):
        new_product_name = input('''Please input new product, 
        Please remember if a product is already exist, u can only edit it:
        first is product name:
        ''')
        new_product_price = input('''now Please input the price:''')
        new_product_num = input('now Plase input quantity:')
        self.sql_to_execute = 'insert into productForTest(name, price, num) value ('+new_product_name+' ,'+new_product_price+','+new_product_num+');'
        self.executeSQL()
        print('done')
        self.init()


    def edit_product_info(self):
        edit_product = input('Plese input what u wanna to edit, Please remember, u can only edit what u have stored:')
        what_change_name = input('''what do u wanna chang: Please u listed format, otherwise i will cry and give u a mistake:
        name, price, quantity
        ''')
        what_change_price = input('input price')
        what_change_num = input('input num')
        self.sql_to_execute = 'update productForTest set name='+what_change_name+', price='+what_change_price+', num='+what_change_num+' where name = '+what_change_name+';'
        print(self.sql_to_execute)
        self.executeSQL()
        print('done')
        self.init()



def main():
    Test_Work()


if __name__ == '__main__':
    main()