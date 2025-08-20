from rest_framework.generics import ListAPIView, RetrieveAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListAPIView):
    """
    View to list all movies.
    """

    # Define the queryset to retrieve all movies
    queryset = Movie.objects.all()

    # Specify the serializer class to use for the response
    serializer_class = MovieSerializer

    # Optionally, you can add permission classes if needed
    # permission_classes = [IsAuthenticated]


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'