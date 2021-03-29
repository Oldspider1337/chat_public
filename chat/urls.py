from django.urls import path

from chat.views import MessagesListView, CreateMessageView, MessageByIdView

urlpatterns = [
    path('create', CreateMessageView.as_view()),
    path('list/', MessagesListView.as_view()),
    path('single/<int:pk>', MessageByIdView.as_view()),
]
