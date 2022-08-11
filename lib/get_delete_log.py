
'''
@file :  get_delete_log.py
@author : 张福卫
@date : 2022/07/10 18:32
'''


import os
def test_remove():
    '''删除日志文件'''
    path = "../log/"  #文件路径
    list = os.listdir(path)  # 列出指定目录下的文件
    for i in list:
        if i:
            file = path + i
            os.remove(file)
    # for i in list:
    #     file = path + i
    #     print(file)
    #     if os.path.isfile(file) == True:   #os.path.isfile判断是否为文件,如果是文件,就删除
    #         os.remove(file)
if __name__ == '__main__':
    test_remove()
    print("---日志已删除---")