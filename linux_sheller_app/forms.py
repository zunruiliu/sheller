# -*- coding:utf-8 -*-

import json
from django import forms


from utils.ips import valid_ip
from dsdk.exceptions import APIError
from utils.errorcode import ERRORCODE
from libs.forms.base import BaseListForm, BaseAdminModelForm


class AddIpForm(forms.Form):
    ip = forms.CharField(label='ip地址', max_length=100, required=True)  # ip地址
    port = forms.CharField(label='端口号', required=True)
    server_name = forms.CharField(label='服务名', required=True)




class IpListForm(BaseListForm):
    status = forms.IntegerField(required=False)
