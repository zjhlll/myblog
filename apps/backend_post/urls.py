# -*- coding=utf-8 -*-
# 2018/5/22,16:57
from django.urls import path,include
from . import views
# from django.views.generic.dates import ArchiveIndexView

urlpatterns = [
    path(r'index/',views.index),
    path(r'details/<int:article_id>/',views.detail),
    path(r'list/<str:category>/',views.get_list),
]
