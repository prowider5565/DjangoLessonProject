from django.urls import path

from users.views import hello_world

urlpatters = [
    path('hello/', hello_world, name='hello_world'),
]