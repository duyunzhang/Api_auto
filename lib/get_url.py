'''
@file: get_url.py
@author: 张福卫
@date : 2022/8/10
'''

import configparser
'''获取配置文件信息'''
conf = configparser.ConfigParser()
conf.read('../config/config.ini')#配置文件路径
'''获取url'''
path_url =conf.get('DEFAULT','url')#url写在配置文件里