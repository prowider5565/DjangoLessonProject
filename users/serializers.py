from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    This serializer can be extended to include fields as needed.
    """

    # username = serializers.CharField(max_length=150)
    # email = serializers.EmailField(max_length=254, required=True)
    # first_name = serializers.CharField(max_length=30, required=False)
    # last_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_superuser",
        ]
