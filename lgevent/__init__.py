# -*- coding: utf-8 -*-
import os
import sys
workspace_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(workspace_path)
import requests
import gevent
import gevent.monkey


def foo1():

    url = 'http://httpbin.org/ip'

    for i in range(50):
        print("{}: {}".format(i, requests.get(url).text))


def foo2():
    # 这里将socket变成异步
    gevent.monkey.patch_socket()

    url = 'http://httpbin.org/ip'

    def hello(i):
        print("{}: {}".format(i, requests.get(url).text))

    tasks = [gevent.spawn(hello, i) for i in range(50)]
    gevent.joinall(tasks)


if __name__ == '__main__':
    foo2()
    import time, arrow
    time.time()