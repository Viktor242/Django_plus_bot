from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer

@api_view(['POST'])
def register_user(request):
    data = request.data
    user, created = TelegramUser.objects.get_or_create(
        user_id=data['user_id'],
        defaults={'username': data.get('username', '')}
    )
    serializer = TelegramUserSerializer(user)
    if created:
        return Response(serializer.data, status=201)
    return Response({'message': 'User is already registered'}, status=200)


@api_view(['GET'])
def get_user_info(request, user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data, status=200)
    except TelegramUser.DoesNotExist:
        return Response({'message': "User not found"}, status=404)


