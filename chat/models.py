from datetime import datetime

from django.db import models


class Message(models.Model):
    text = models.TextField(verbose_name='text', max_length=100, null=True, blank=True)
    author = models.EmailField(verbose_name='author', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
