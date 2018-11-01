# coding=utf-8


# scrapy/http/response.py
'''封装Response对象'''


class Response(object):
    '''框架内置Response对象'''

    def __init__(self, url, status_code, headers, body):
        self.url = url  # 响应url
        self.status_code = status_code  # 响应状态码
        self.headers = headers  # 响应头
        self.body = body  # 响应体
