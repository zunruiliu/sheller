# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 系统包
import datetime
import os


# 第三方包
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


# 自己写的包
from .models import IpModel
from .forms import AddIpForm, IpListForm
from libs.response import http_response
from libs.errorcode import CommonError, StatusCode
from utils.errorcode import ERRORCODE
from linux_sheller_app import models


def get_server_view(request):
    server_list = models.IpModel.objects.all()
    return render(request, 'html/server_list.html', {'server_list': server_list})


def add_server_view(request):
    if request.method == 'GET':
        return render(request, 'html/add_server.html')
    elif request.method == 'POST':
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        server_name = request.POST.get('server_name')
        models.IpModel.objects.create(ip=ip, port=port, server_name=server_name)
        return redirect(get_server_view)


def edit_server_view(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.IpModel.objects.filter(id=nid).first()
        print obj
        return render(request, 'html/edit_server.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        server_name = request.POST.get('server_name')
        models.IpModel.objects.filter(id=nid).update(ip=ip, port=port, server_name=server_name)
        return redirect(get_server_view)


def delete_server_view(request):
    nid = request.GET.get('nid')
    models.IpModel.objects.filter(id=nid).delete()
    return redirect(get_server_view)


def deploy_server_view(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.IpModel.objects.filter(id=nid).first()
        return render(request, 'html/deploy_server.html', {'obj': obj})
    elif request.method == 'POST':
        os.system('/Users/liuzunrui/Documents/dev/myproject/sheller/linux_sheller/sheller_project/data/a.sh')
        return redirect(check_logs_view)


def check_logs_view(request):
    nid = request.GET.get('nid')

    return render(request, 'html/check_logs.html')

