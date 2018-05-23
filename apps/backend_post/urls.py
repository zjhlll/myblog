# -*- coding=utf-8 -*-
# 2018/5/22,16:57
from django.urls import path,include
from .views import *
# from django.views.generic.dates import ArchiveIndexView

urlpatterns = [
    path(r'index',index),
]
