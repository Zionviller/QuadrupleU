from django.db import models
from apps.login_reg.models import User

class Outfit(models.Model):
    imageURL = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "outfits", on_delete=models.CASCADE)
