# -*- coding:utf-8 -*-
from po.basepage import BasePage

class TestApiRequest(BasePage):
    req_data = {
        "method": 'get',
        "url": "http://aaa:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_encode(self):
        """
        加密解密
        :return:
        """
        r=self.send(self.req_data)
        print(r)


