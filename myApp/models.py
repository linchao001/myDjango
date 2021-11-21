# encoding: utf-8

from django.db import models

# Create your models here.
class Message(models.Model):
    time = models.DateTimeField("留言时间", auto_now=True)
    msg = models.TextField("留言内容",max_length=3000)