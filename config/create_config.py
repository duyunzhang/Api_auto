'''
@file: create_config.py
@author: 张福卫
@date : 2022/8/11
'''

import configparser


def create_config(deft, key, value):
    con = configparser.ConfigParser()

    con.add_section(deft)  # 添加模块
    con.set(deft, key, value)  # 创建配置文件信息

    with open('../config/config.ini', 'a', encoding='utf-8') as f:
        con.write(f)


if __name__ == '__main__':
    deft = 'mysql'
    key = 'name'
    value = 'zhangsan'
    create_config(deft,key,value)
