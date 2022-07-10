'''
@file :  get_log.py
@author : 张福卫
@date : 2022/07/10 17:47
'''


import logging
import time

class Log(object):

    def log(self):
        #创建日志器
        logger=logging.getLogger('logger')
        #设置日志输出等级
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            #创建处理器
            sh=logging.StreamHandler()

            # F:\pythonProject4\log
            fh=logging.FileHandler(filename="../log\\\{}_log.txt".format(time.strftime("%Y_%m_%d")),encoding="utf-8",mode="a")
            # fh=logging.FileHandler(filename="F:\\pythonProject4\\log\\".format(time.strftime("%Y_%m_%d")),encoding="utf-8",mode="a")

            # 创建格式器
            formator=logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s")
            sh.setFormatter(formator)
            fh.setFormatter(formator)

            #增加处理器
            logger.addHandler(sh)
            logger.addHandler(fh)

        return logger