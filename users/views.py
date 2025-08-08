from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer



class EXampleAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.filter(is_active=True)
    model = User
    lookup_field = "username"
    pagination_class = object
    filterset_class = object

    def get_queryset(self):
        deleted= self.request.query_params.get("deleted", False)
        return super().get_queryset().filter(is_active=deleted)


    def post(self, request, *args, **kwargs):
       return super().post(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)



# Function based
""" Class based views
        Generic api view
        APIView
        Viewset
        ModelViewSet
        ListAPIView, CreateAPIView, ListCreateAPIView RetrieveAPIView, UpdateAPIView, DestroyAPIView
"""


@api_view(["POST"])
def register(request):
    user_data = UserSerializer(data=request.data)
    user_data.is_valid(raise_exception=True)
    print(user_data.validated_data)
    if user_data.validated_data.get("is_superuser", False):
        User.objects.create_superuser(**user_data.validated_data)
    else:
        User.objects.create_user(is_active=False, **user_data.validated_data)
    return Response(data={"msg": "Hello, World!"}, status=status.HTTP_200_OK)
