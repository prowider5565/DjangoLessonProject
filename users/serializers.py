from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    Serializer for User model.
    This serializer can be extended to include fields as needed.
    """
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254, required=False)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
