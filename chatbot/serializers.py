from rest_framework import serializers
from chatbot.models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = [
            "id",
            "user_message",
            "bot_response",
            "created_at",
        ]
