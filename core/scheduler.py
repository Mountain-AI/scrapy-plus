# coding=utf-8
# 爬虫框架/core/scheduler.py
"""调度器模块封装"""

# 利用six模块实现py2与py3的兼容
from six.moves import queue


class Scheduler:
    """
    1,缓存请求对象,并为下载器提供请求对象,实现请求的调度
    2,对请求对象进行去重
    """
    def __init__(self):
        self.queue = queue.Queue()

    def add_request(self, request):
        """添加请求对象"""
        # if self._filter_request(request):
        self.queue.put(request)

    def get_request(self):
        """获取一个请求对象并返回"""
        request = self.queue.get()
        return request

    def _filter_request(self, request):
        """请求去重"""
        # 暂时不实现
        pass




