'''
@file :  test_response_format.py
@author : 张福卫
@date : 2022/07/09 12:40
'''

import json

def get_response(results):
    '''将接口返回值转换成json格式'''
    m = json.dumps(results.json(), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
    print(m)

