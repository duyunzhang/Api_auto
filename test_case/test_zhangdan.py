'''
@file :  test_zhangdan.py
@author : 张福卫
@date : 2022/07/08 18:16
'''

import requests

from lib.get_writ_file import test_write_file
from lib.get_response_key import *
from lib.get_response_format import *
from lib import get_log
log= get_log.Log().log()

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
        test_write_file(get_response1(res))
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
        self.assertEqual('zhongtong',valus)
        get_response(res) #打印返回结果
        test_write_file(get_response1(res))
        log.info("url:{}，"
                 "请求参数:{},"
                 "请求结果:{}".format(url, params,get_response1(res)))

        print('传参值\n' + str(params))


if __name__ == '__main__':
    unittest.main()
