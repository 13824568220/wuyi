# -*- coding:utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth
import base64

class TestCooke:

    def test_header_cookie(self):
        """
        通过请求头信息传递cookie
        :return:
        """
        url='https://httpbin.testing-studio.com/cookies'
        header={"Cookie": "aaa",
                'User-Agent': 'wuyi'
                }
        r=requests.get(url=url,headers=header,verify=False)
        print(r.request.headers)
    def test_cookie_cookies(self):
        """
        通过请求的关键字参数cookies传递
        :return:
        """
        url='https://httpbin.testing-studio.com/cookies'
        header={
                'User-Agent': 'wuyi'
                }
        cookie_data={"age": "23",
                     "set": "nan"}
        r=requests.get(url=url,headers=header,cookies=cookie_data,verify=False)
        print(r.request.headers)

    def test_auth(self):
        """
        http basic认证
        :return:
        """
        url="https://httpbin.testing-studio.com/basic-auth/apple/12345"
        r=requests.get(url=url,auth=HTTPBasicAuth("apple","12345"),verify=False)
        print(r.text)
        assert r.status_code==200


