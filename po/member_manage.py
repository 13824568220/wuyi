# -*- coding:utf-8 -*-
import requests
from faker import Faker

from po.basepage import BasePage


class MemberManage(BasePage):
    faker=Faker("zh_CN")
    name=faker.name() # 名字
    userid=faker.numerify() # 随机3位数字
    phone=faker.phone_number() # 手机号
    def add_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": f"2021-{self.userid}",
            "name": f"{self.name}",
            "mobile": f"{self.phone}",
            "department": [1] }
        r = requests.post(url=url, json=data, verify=False)
        print(f"{self.name}")
        print(f"2021{self.userid}")
        return r.json()

    def delete_member(self):
        pass
    def update_member(self):
        pass
    def query_member(self):
        pass