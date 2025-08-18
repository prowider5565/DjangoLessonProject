from django.urls import path

from users.views import register, get_my_details

urlpatterns = [
    path("register/", register, name="hello_world"),
    path("me/", get_my_details),
]
