# -*- coding:utf-8 -*-
"""
演练环境：
http://httpbin.testing-studio.com
requests.get请求失败原因分析：
ssl验证失败
解决方案：
在使用requests发送请求的时候加上verify这个参数并设置为False
"""
import json

import requests
from jsonpath import jsonpath
from jsonschema import validate
from requests_xml import XMLSession


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get", verify=False)
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code==200
    def test_demo2(self):
        r=requests.get('https://api.github.com/events',verify=False)
        print(r.text)
        assert r.status_code == 200

    def test_Get_Query(self):
        """
        Get Query请求
        :return:
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get('https://httpbin.org/get', params=payload, verify=False)
        print(r.text)
        assert r.status_code == 200

    def test_form(self):
        """
        Form请求参数构造
        :return:
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("https://httpbin.org/post", data=payload,verify=False)
        print(r.text)
        assert r.status_code==200


    def test_hearders(self):
        """
        普通的header:
        :return:
        """
        headers = {'user-agent': 'aa'}
        r = requests.get("https://httpbin.org/get", headers=headers,verify=False)
        print(r.text)
        print(r.json())
        print(r.request)
        assert r.status_code==200
        assert r.json()['headers']['User-Agent']=='aa'

    def test_post_json(self):
        """
        Form请求参数构造
        :return:
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("https://httpbin.org/post", json=payload,verify=False)
        print(r.text)
        print(r.json())
        assert r.json()['json']['key1']=="value1"
        assert r.status_code==200

    def test_hogwarts_json(self):
        r=requests.get("https://ceshiren.com/categories.json",verify=False)
        print(r.text)
        print(r.json())
        # 把输出的json写入文件中
        with open('./data.json',"w",encoding='utf-8')as f:
            f.write(str(r.json()))
        assert r.json()['category_list']['categories'][0]['name']=="开源项目"

    def test_hogwarts_json2(self):
        r=requests.get("https://ceshiren.com/categories.json",verify=False)
        print(r.text)
        print(r.json())
        # 把输出的json写入文件中
        with open('./data.json',"w",encoding='utf-8')as f:
            f.write(str(r.json()))
        print(jsonpath(r.json(),'$..name'))
        assert jsonpath(r.json(),'$..name')[0]=='开源项目'

    def test_xml(self):
        session=XMLSession()
        r=session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss',verify=False)
        print(r.xml.links)
        # 把输出的json写入文件中
        with open('./data2.json', "w", encoding='utf-8')as f:
            f.write(str(r.xml.links))
        item=r.xml.xpath('//item',first=True)
        print(item.text)

    def test_schema(self):
        """
        schema校验
        :return:
        """

        url="https://testerhome.com/api/v3/topics.json"
        data=requests.get(url,params={'limit': '2'},verify=False).json()
        print(data)
        schema=json.load(open("topic_schema.json",encoding='utf-8'))
        validate(data,schema=schema)