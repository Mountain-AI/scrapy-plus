# coding=utf-8
# 爬虫中间件


class SpiderMiddleware:
    """完成爬虫中间件的封装"""
    def process_request(self, request):
        """
        实现对request的处理
        :param request: 请求对象
        :return: 返回请求
        """
        print("爬虫中间件:process_request")
        return request

    def process_response(self, response):
        """
        实现对response的处理
        :param response: 响应对象
        :return: 返回响应
        """
        print("爬虫中间件:process_response")
        return response


