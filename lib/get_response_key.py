'''
@file :  get_response_key.py
@author : 张福卫
@date : 2022/07/08 18:26
'''
import  jsonpath
def getkey(res,key):
    '''断言_获取返回值字段值'''
    if res != '':
        try:
            res = res.json()  # 将返回值转会成json格式
            value = jsonpath.jsonpath(res, '$..{}'.format(key))  # '$..{0}'从返回值的根目录开始遍历  key:要遍历的字段
            if value :
                if len(value) == 1:
                    return value[0]  #返回字段值的格式是以列表形式出现，通过遍历方法给出
            return value

        except Exception as e:
            return e
    else:
        return f'没有当前{key}字段值'