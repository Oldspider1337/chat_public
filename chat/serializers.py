from rest_framework import serializers

from chat.models import Message


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'author')
    #
    # def validate(self, attrs):
    #     print('huy')
    #     if len(attrs.text) > 100:
    #         raise serializers.ValidationError('ban')


class MessagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'author', 'create_date')
