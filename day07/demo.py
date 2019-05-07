#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" This is a demo module... """

__author__ = 'Tom'

import sys   # 装载sys 模块


def _fn_private():
    print('This is a private function...')


def fn_test():
    """ This is a test function """
    print(sys.argv)  # 获取命令行参数
    _fn_private()


if __name__ == '__main__':
    fn_test()

# print('demo.py', __name__)
