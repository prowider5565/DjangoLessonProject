from django.urls import path

from users.views import RegisterAPIView, get_my_details

urlpatterns = [
    # path("register/", register, name="hello_world"),
    path("me/", get_my_details),
    path('register/', RegisterAPIView.as_view(), name='register_post'),  # POST uchun
]
