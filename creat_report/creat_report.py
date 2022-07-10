'''
@file :  report.py
@author : 张福卫
@date : 2022/07/08 19:56
'''

import HTMLTestRunner
import unittest
import time
import BeautifulReport
class report:

    def test_creat_BFreport(self):
        '''BeautifulReport测试报告'''

        #执行文件路径
        case_path = '../test_case\\'

        #加载用例
        '''discover 遍历指定目录下所有  test_*.py 的用例'''
        dis = unittest.defaultTestLoader.discover(case_path, 'test_zhangdan.py')

        #生成报告时间

        # 生成报告时间
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

        # 定义报告文件名称
        reportname = now + 'report_bf.py'

        #执行用例生成报告
        report_path = '../html_report\\'  #报告存储地址

        BeautifulReport.BeautifulReport(dis).report(filename=reportname, report_dir=report_path, description='订单状态')

    def test_creat_HTreport(self):
        '''HTMLTestRunner测试报告'''
        #执行文件路径
        # case_path = 'F:\\test_API_Auto\\read_excel\\'
        case_path = '../test_case\\'

        #加载用例
        # dis = unittest.defaultTestLoader.discover(case_path,'test_request.py')
        '''discover 遍历指定目录下所有  test_*.py 的用例'''
        dis = unittest.defaultTestLoader.discover(case_path,'test_zhangdan.py')

        #生成报告时间
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

        '''生成报告'''

        #定义报告文件名称
        reportname = now + 'report.html'

        #生成报告路径
        report_path = '../html_report\\' + reportname

        #执行用例生成报告
        # fb = open(report_path,'w',encoding='utf-8')
        fb = open(report_path, "w", encoding='utf-8')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fb,title="测试报告",description="用例执行情况")

        m = runner.run(dis)
        return m


if __name__ == '__main__':
    report().test_creat_BFreport()















