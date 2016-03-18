#!/usr/bin/python

import pymysql
import os

# CONFIG
code_file_path = 'code'
host = '127.0.0.1'
user = 'test_user'
db = 'test_db'
pwd = 'test_passwd'
table = 'code_table'

try:
    f = open(code_file_path)
    conn = pymysql.connect(host=host, port=3306,
                           user=user, passwd=pwd, db=db)
    cur = conn.cursor()
    cur.execute("create table "+table+"(id int primary key auto_increment,\
                                         code char(128) not null)\
                ")
    conn.commit()
    for code in f:
        sql = 'INSERT INTO `code_table` (code) VALUE(%s)'
        cur.execute(sql, code.strip('\n'))
        conn.commit()
finally:
    cur.close()
    conn.close()
    f.close()
