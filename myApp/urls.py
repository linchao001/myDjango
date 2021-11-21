# encoding: utf-8

from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
urlpatterns = [
    re_path(r'^msg/(?P<index>[0-9]+)/$', views.MessageList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)