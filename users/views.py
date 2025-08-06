from rest_framework.response import Response
from rest_framework import status


def hello_world(request):
    return Response(data={"msg": "Hello, World!"}, status=status.HTTP_200_OK)
