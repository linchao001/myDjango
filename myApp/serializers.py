# encoding: utf-8
from rest_framework import serializers

from myApp.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('time', 'msg')