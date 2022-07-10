'''
@file :  test_zhangdan.py
@author : 张福卫
@date : 2022/07/08 18:16
'''

import requests
from lib.test_getkey import *
from lib.test_response_format import *

import unittest


class test_ceshi(unittest.TestCase):

    def setUp(self):
        print('{}开始执行用例'.format(self))

    def tearDown(self):
        print('{}结束执行用例'.format(self))
    def test_tt(self):
        '''获取返回值'''
        url = 'http://www.kuaidi100.com/query'
        params = {'type': 'zhongtong',
                  'postid': '75527538262087'

                  }
        res = requests.get(url=url, params=params)
        valus = getkey(res, 'com')
        # print(m+'\n'+'-*-*'*10)
        print('com的字段值'+ valus)
        return valus

        # res = res.json()
        # results = jsonpath.jsonpath(res, '$..{0}'.format('contet'))
        # if len(results)==1:
        #     print(results[0])
        # elif len(results) >1:
        #     for i in results:
        #         print(i)

    def test_canshuhua(self):
        '''参数化'''
        url = 'http://www.kuaidi100.com/query'
        params = {'type': test_ceshi.test_tt(self),
                  'postid': '75527538262087'

                  }
        res = requests.get(url=url, params=params)
        valus = getkey(res,'com')
        self.assertEqual('zhongtonG',valus)
        get_response(res)

        print('传参值\n' + str(params))


if __name__ == '__main__':
    unittest.main()
