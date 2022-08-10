'''
@file :  test_zhangdan.py
@author : 张福卫
@date : 2022/07/08 18:16
'''


import requests,unittest
from lib.get_url import path_url
from lib.get_writ_file import test_write_file
from lib.get_response_key import *
from lib.get_response_format import *
from ddt import ddt,file_data
from lib import get_log
log= get_log.Log().log()

@ddt
class test_ceshi(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.com=None

    @file_data('../data/dingdan.yaml')
    def test_1(self,**kwargs):
        '''订单详情'''
        url = path_url
        params = kwargs['data']
        res = requests.get(url=url, params=params)
        p=json.dumps(params,ensure_ascii=False,indent=4)
        describe=kwargs['describe']
        print('入参方式：',describe,'\n入参：',p)
        get_response(res)
        valus = getkey(res, 'com')
        test_ceshi.com=valus



    def test_2(self):
        '''参数化'''
        url = 'http://www.kuaidi100.com/query'
        params = {'type': self.com,
                  'postid': '75527538262087'

                  }
        res = requests.get(url=url, params=params)
        valus = getkey(res,'com')
        test_ceshi.com=valus

        get_response(res) #打印返回结果
        test_write_file(get_response1(res))
        log.info("url:{}，"
                 "请求参数:{},"
                 "请求结果:{}".format(url, params,get_response1(res)))

        print('传参值\n' + str(params))


if __name__ == '__main__':
    unittest.main()
