from django.shortcuts import render
from django.views import View
from rest_framework import generics

from chat.models import Message
from chat.pagination import CustomPagination
from chat.serializers import CreateMessageSerializer, MessagesListSerializer


class CreateMessageView(generics.CreateAPIView):
    serializer_class = CreateMessageSerializer


class MessagesListView(generics.ListAPIView):
    serializer_class = MessagesListSerializer
    pagination_class = CustomPagination
    queryset = Message.objects.all()


class MessageByIdView(generics.RetrieveAPIView):
    serializer_class = MessagesListSerializer
    queryset = Message.objects.all()

