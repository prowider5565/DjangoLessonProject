from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from users.serializers import UserSerializer


@api_view(['POST'])
def hello_world(request):
    user_data = UserSerializer(data=request.data)
    user_data.is_valid(raise_exception=True)
    print(user_data.validated_data)
    return Response(data={"msg": "Hello, World!"}, status=status.HTTP_200_OK)
