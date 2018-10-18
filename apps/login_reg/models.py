from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 255)
    friendCode = models.CharField(max_length = 14)
    password = models.CharField(max_length = 32)
