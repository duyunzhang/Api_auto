import os


def test_remove():
    '''删除报告文件'''
    path = "../html_report/"  # 文件路径
    list = os.listdir(path)  # 列出指定目录下的文件
    for i in list:
        print(i)
        file = path + i
        if os.path.isfile(file) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除
            os.remove(file)


if __name__ == '__main__':
    test_remove()
    print("---日志已删除---")
