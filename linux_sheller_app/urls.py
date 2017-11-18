# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^get_server$', views.get_server_view, name='index'),
    url(r'^add_server', views.add_server_view, name='add_server'),
    url(r'^edit_server', views.edit_server_view, name='edit_server'),
    url(r'^delete_server.html', views.delete_server_view, name='delete_server'),
    url(r'^deploy_server', views.deploy_server_view, name='deploy_server'),
    # url(r'^deploy_server_action', views.deploy_server_action_view, name='delete_server_action_view')
    url(r'^check_log', views.check_logs_view, name='check_logs')
]