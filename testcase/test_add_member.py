# -*- coding:utf-8 -*-
"""
vuzS2Z0rE7TiBlH9P0OPCRkIp6Hf7WlSwVc6LWARf26YbeLDapBqBWxayFnLbotl43pD6cuGLnNUEkF1XyZiMWxLoP4KoAonO0dUqsTpDXh7hMJkK5_s2ejRaJGZSOkoyPqWhUyH8QcOKv2HX9sfjArMzV0mj5DN0jy3HSeXb4mDZmk9H7P_ch-Oo8elqs-cYgYCfcOcqurJWqmjPmoFxA
https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww0e005a984a50a3a7&corpsecret=PWJNqCfLezTNfzlWgGQZ3Gl1E0y59rI84Kg2N8gkfok
"""
import requests

from po.member_manage import MemberManage


class TestAddMember:
    def test_add_mem(self):
        add_member=MemberManage()
        r=add_member.add_member()
        assert r['errmsg'] in "created"


