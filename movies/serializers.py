from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for the Movie model.
    """

    class Meta:
        model = Movie
        fields = '__all__'  # Serialize all fields of the Movie model