from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chatbot.models import ChatMessage
from chatbot.rag.pipeline import rag_pipeline

# class ChatView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             message = request.data.get('message')
#             if not message:
#                 return Response({"error": "message field is required"}, status=400)

#             response = rag_pipeline(message)

#             # Debug print
#             print("Message:", message)
#             print("Response:", response)

#             # Save to DB safely
#             ChatMessage.objects.create(
#                 user=request.user,
#                 user_message=message,
#                 bot_response=response
#             )

#             return Response({"response": response})

#         except Exception as e:
#             print("ChatView error:", e)
#             return Response({"error": str(e)}, status=500)


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({"error": "message field is required"}, status=400)

        response = rag_pipeline(message)  # Replace Echo with RAG/OpenAI

        # Save to DB
        ChatMessage.objects.create(
            user=request.user,
            user_message=message,
            bot_response=response
        )

        return Response({"response": response})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from chatbot.models import ChatMessage
from chatbot.serializers import ChatMessageSerializer

class ChatHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chats = ChatMessage.objects.filter(
            user=request.user
        ).order_by("-created_at")

        serializer = ChatMessageSerializer(chats, many=True)
        return Response(serializer.data)
