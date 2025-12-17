from datetime import timedelta
from django.utils import timezone
from chatbot.models import ChatMessage

def delete_old_chats():
    ChatMessage.objects.filter(
        created_at__lt=timezone.now() - timedelta(days=30)
    ).delete()
