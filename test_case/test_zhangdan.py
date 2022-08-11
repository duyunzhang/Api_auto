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

    def assigment(self,kwargs):
        '''赋值函数'''
        for key,value in kwargs.items():
            if type(value) is dict:
                self.assigment(value) #如果value是字典格式，进行递归
            else:
                if value: #如果yaml文件字段有传值，跳过
                    pass
                else:
                    kwargs[key] = getattr(self,key) #没有传值，就赋值
        return kwargs

    @classmethod
    def setUpClass(cls) -> None:
        cls.com=None
        cls.nu:None
        cls.condition:None
        cls.message:None

    @file_data('../data/dingdan.yaml')
    def test_1(self,**kwargs):
        '''订单详情'''
        url = path_url
        params = kwargs['data']
        res = requests.get(url=url, params=params)
        p=json.dumps(params,ensure_ascii=False,indent=4)
        print('用例：',kwargs['describe'],'\n入参：',p)
        get_response(res)
        valus = getkey(res, 'com')
        test_ceshi.com=valus

    @file_data('../data/test_2.yaml')
    def test_2(self, **kwargs):
        '''订单详情'''
        url = path_url
        params = kwargs['data']
        res = requests.get(url=url, params=params)
        condition = getkey(res, 'condition')
        nu = getkey(res, 'nu')
        message = getkey(res, 'com')
        test_ceshi.condition = condition
        test_ceshi.nu = nu
        test_ceshi.message = message
        get_response(res)

    def test_3(self):
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
        log.info("'"
                 "\nurl:{}"
                 "\n请求参数:{},"
                 "\n请求结果:{}".format(url, params,get_response1(res)))

        print('传参值\n' + str(params))
    @file_data('../data/canshu.yaml')
    def test_4(self,**kwargs):
        d = self.assigment(kwargs)
        d=json.dumps(d,ensure_ascii=False,sort_keys=True,indent=4)

        print(d)


if __name__ == '__main__':
    unittest.main()
