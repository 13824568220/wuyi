# -*- coding:utf-8 -*-
import base64
import json
import requests
from po.utils import read_yaml, get_token


class BasePage:
    env = read_yaml()
    token=None # 类变量，多个实例，类可以共用这个变量
    def __init__(self):
        if self.token is None:
            self.token=get_token()

    def send(self,data: dict):
        data['url']=str(data['url']).replace('aaa',self.env["aa"][self.env["default"]])
        res=requests.request(data['method'],data['url'],headers=data['headers'])
        # base64解密
        if data['encoding']=='base64':
            return json.loads(base64.b64decode(res.content))
        # 把加密后的响应值发送第三方服务，让第三方解密后返回解密信息
        elif data['encoding']=='private':
            return requests.post("url",data=res.content)
