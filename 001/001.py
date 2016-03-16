#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import Random
import sys
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
r = Random()
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
length = len(chars) - 1
f = open("test",'w')

def generate_20_code():
    code = ''
    for c in xrange(0,20):
        code += chars[r.randint(0,length)]
    return code

def generate_code(num):
    code = []
    for x in xrange(0, num):
        temp_code = generate_20_code()
        x, y = 0, 5
        code_1 = ''
        for step in xrange(0,5):
            code_1 += temp_code[x:y]
            x, y = y, y+5
            code_1 += '-'
        code_1 = code_1[:23]
        code.append(code_1)
        temp_code = ''
    return code

for string in generate_code(200):
    f.write(string+'\n')
f.close()



# code_2 = []
# for x in xrange(1,50):
#     # code_2.append(random_str())
#     code_2.append(generate_20_code())
# print code_2