# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from dsdk.mixins import TimeModelMixin, EditorModelMixin


class IpModel(TimeModelMixin):
    ip = models.CharField(u'服务器IP', max_length=100)
    port = models.CharField(u'端口号', max_length=10)
    server_name = models.CharField(u'服务名', max_length=200)

    class Meta:
        db_table = 'linux_sheller_app_ipmodel'
        unique_together = [['ip']]
        index_together = [['created_time'], ['server_name']]
