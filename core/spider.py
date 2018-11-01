# coding=utf-8

# 爬虫框架/core/spider.py
"""爬虫组件封装"""
from scrapy_plus.item import Item
from scrapy_plus.http.request import Request


class Spider:
    """
    1,构建请求信息,生成请求对象
    2,解析响应返回数据Item或者新的请求对象
    """
    start_url = "http://www.baidu.com"  # 以百度为例,默认的初始请求地址

    def start_requests(self):
        """构建初始请求对象并返回"""
        return Request(self.start_url)

    def parse(self, response):
        """
        解析响应
        返回新的请求对象或者数据对象
        """
        return Item(response.body)