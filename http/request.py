# coding=utf-8

# scrapy/http/request.py
'''封装Request对象'''


class Request(object):
    '''框架内置请求对象，设置请求信息'''

    def __init__(self, url, method='GET', headers=None, params=None, data=None):
        self.url = url  # 请求地址
        self.method = method  # 请求方法
        self.headers = headers  # 请求头
        self.params = params  # 请求参数
        self.data = data  # 请求体
