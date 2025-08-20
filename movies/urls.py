from django.urls import path

from movies.views import MovieDetailView, MovieListView

urlpatterns = [
    path("list/", MovieListView.as_view(), name="movie-list"),
    path("detail/<int:id>/", MovieDetailView.as_view(), name="movie-detail"),
]
