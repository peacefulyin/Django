#coding=utf-8
from django.conf.urls import url
from myblog import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^text/$',views.text),
    url(r'^test/$', views.test),
    url(r'^getjson/(\d+)$', views.return_json),
    url(r'^about/$',views.about),
    url(r'^artical/(.*)$',views.show_artical),
    ]
