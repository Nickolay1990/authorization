from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
