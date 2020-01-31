# -*- coding: utf-8 -*-

from .. import app
import time
import requests
import gevent
import asyncio
import json
from datetime import datetime
# from aiohttp import ClientSession
from logzero import logger


count = 0

result_json = ""

push_url = 'https://3g.dxy.cn/newh5/view/pneumonia_peopleapp?from=timeline&isappinstalled=0'
# 实时播报地址


def fetch_async(method, url, req_kwargs):
    global count
    global push_url
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

    parameters = {}
    parameters['body'] = '数据汇总：\n标题: {title}\n执行时间: {timestamp}\n实时时间: {modifyTime}\n确诊: {confirmedCount}例\n疑似: {suspectedCount}例\n死亡: {curedCount}例\n实时播报地址: {push_url}' \
        .format(title=statistics_message['virus'], timestamp=get_current_date(fmt="%Y-%m-%d %H:%M:%S"),modifyTime=modifyTime, confirmedCount=statistics_message['confirmedCount'],
                suspectedCount=statistics_message['suspectedCount'], curedCount=statistics_message['curedCount'], push_url=push_url)

    logger.info(parameters['body'])
    send_wechat_message(parameters['body'])
    # result_json = json.dumps(message_json,indent=4)





# 定义异步函数
async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    for i in range(5):
        loop.run_until_complete(hello())


loop = asyncio.get_event_loop()


# @app.task
# def test_get_request():
#
#     ##### 发送请求 #####
#
#     # 获取疫情接口
#     gevent.joinall([
#         # 这里spawn是3个任务[实际是3个协程]，每个任务都会执行fetch_async函数
#         gevent.spawn(fetch_async, method='get', url='https://www.baidu.com',
#                      req_kwargs={})
#         ,
#         gevent.spawn(fetch_async, method='get', url='https://www.sina.cn',
#                      req_kwargs={}
#                      )])
#
#     return "test_get_request"


@app.task
def test_get_request_2019_nCoV():

    logger.info("############ Start ###########")

    url = 'https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia'

    ##### 发送请求 #####
    gevent.joinall([
        # 这里spawn是3个任务[实际是3个协程]，每个任务都会执行fetch_async函数
        gevent.spawn(fetch_async, method='get', url=url,req_kwargs={})
        ]
    )

    logger.info(result_json)

    return result_json


def get_current_date(fmt="%Y-%m-%d"):
    """ get current date, default format is %Y-%m-%d
    """
    return datetime.now().strftime(fmt)

def send_wechat_message(message_text):
    """"
    发送企业微信机器人消息
    :param platform:
    :param app_version:
    :param tag:
    :param env:
    :param app_path:
    :return:
    """



    message_text = '*************************** 实时疫情播报 ***************************************' + '\n' + \
                   message_text + '\n' + \
                   '***************************************************************************************'
    try:

        webhook_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a0a3bd2c-268c-4134-ba67-ae83a8fe1d68"  # 单独的接口自动化测试群
        data = {
            "msgtype": "text",
            "text": {
                "content": message_text,
            }
        }
        logger.info(json.dumps(message_text,indent=4))
        r = requests.post(webhook_api, json=data, verify=False)
        logger.info(str(r.status_code))
    except Exception as e:
        logger.error(str(e))