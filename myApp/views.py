# encoding: utf-8
# Create your views here.
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from myApp.models import Message
from myApp.serializers import MessageSerializer
from myApp.utils.user_time import user_time


class MessageList(APIView):
    '''
    分页查询评论，每页10条
    插入一条评论
    '''
    def get(self, request, index, format=None):
        index = int(index) # url参数，每次查询的索引
        count = 3 # 每次查询的数量
        msg = Message.objects.all().order_by("-time")[(index-1)*count : index*count]
        serializer = MessageSerializer(msg, many=True)

        return Response(serializer.data)

    def post(self, request, index, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MessageList(generics.ListCreateAPIView):
#
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


