# coding=utf-8

# scrapy_plus/core/downloader.py
'''下载器组件'''
import requests
from scrapy_plus.http.response import Response


class Downloader(object):
    """
    根据请求对象(Request)，发起HTTP、HTTPS网络请求，
    拿到HTTP、HTTPS响应，构建响应对象(Response)并返回
    """

    def get_response(self, request):
        '''发起请求获取响应的方法'''
        # 1. 根据请求对象，发起请求，获取响应
        #    判断请求方法：
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers, params=request.params, data=request.data)
        else:
            # 如果方法不是get或者post，抛出一个异常
            raise Exception("不支持的请求方法")
        # 2. 构建响应对象,并返回
        return Response(resp.url, resp.status_code, resp.headers, resp.content)
