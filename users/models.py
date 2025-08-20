from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    You can add additional fields here if needed.
    """

    username = models.CharField(max_length=120, unique=False)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"


# class Address(models.Model):
#     user = models.ForeignKey(
#         to=User, on_delete=models.CASCADE, related_name="addresses"
#     )
#     city = models.CharField(max_length=300)
