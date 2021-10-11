# -*- coding:utf-8 -*-
import requests
import yaml

def read_yaml():
    with open("../data/data_yaml.yml")as f:
        env=yaml.safe_load(f)
    return env

def get_token():
    """
    获取token
    :return:
    """
    corpid = "ww0e005a984a50a3a7"
    corpsecret = "PWJNqCfLezTNfzlWgGQZ3Gl1E0y59rI84Kg2N8gkfok"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r=requests.get(url=url,verify=False)
    # 返回原生的文本格式
    #print(r.text)
    # 转成json格式
    return  r.json()['access_token']