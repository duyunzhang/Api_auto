'''
@file :  get_writ_file.py
@author : 张福卫
@date : 2022/07/10 18:21
'''
def test_write_file(self):
    '''打印返回结果'''
    import time
    today = time.strftime("%Y_%m_%d %Hh %Mm %Ss", time.localtime()) #获取当前时间

    name = today +' log.txt' #拼接以时间开头区分的文件名称

    address = "../log\\" + name #保存路径

    #addr = "../" + date  #拼接文件路径名  [../] 表示在当前项目根目录下

    with open(address,'a',encoding='utf8') as f:
        f.write(self)