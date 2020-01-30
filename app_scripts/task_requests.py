# -*- coding: utf-8 -*-

from .. import app
import time
import requests
import gevent
import asyncio
import json
# from aiohttp import ClientSession
from logzero import logger


count = 0

result_json = ""

def fetch_async(method, url, req_kwargs):
    global count
    count = count + 1
    response = requests.request(method=method, url=url, **req_kwargs)
    logger.info("################ {0}-{1}-{2} ################".format(response.url, response.status_code, count))

    statistics_message = response.json()['data']['statistics']

    modifyTime = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(int(statistics_message['modifyTime'] / 1000)))

    global result_json
    result_json = {'url':str(response.url),
            'status_code':response.status_code,
            'virus': statistics_message['virus'],
            'confirmedCount':statistics_message['confirmedCount'],
            'suspectedCount': statistics_message['suspectedCount'],
            'curedCount': statistics_message['curedCount'],
            'modifyTime': modifyTime
            }


    # result_json = json.dumps(message_json,indent=4)





# 定义异步函数
async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    for i in range(5):
        loop.run_until_complete(hello())


loop = asyncio.get_event_loop()


@app.task
def test_get_request():

    ##### 发送请求 #####

    # 获取疫情接口
    gevent.joinall([
        # 这里spawn是3个任务[实际是3个协程]，每个任务都会执行fetch_async函数
        gevent.spawn(fetch_async, method='get', url='https://www.baidu.com',
                     req_kwargs={})
        ,
        gevent.spawn(fetch_async, method='get', url='https://www.sina.cn',
                     req_kwargs={}
                     )])

    return "test_get_request"


@app.task
def test_get_request_2019_nCoV():

    url = 'https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia'

    ##### 发送请求 #####
    gevent.joinall([
        # 这里spawn是3个任务[实际是3个协程]，每个任务都会执行fetch_async函数
        gevent.spawn(fetch_async, method='get', url=url,req_kwargs={})
        ]
    )

    logger.info(result_json)

    return result_json
