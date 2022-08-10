'''
@file: get_url.py
@author: 张福卫
@date : 2022/8/10
'''

import configparser
conf = configparser.ConfigParser()
conf.read('../config/config.ini')
path_url =conf.get('DEFAULT','url')