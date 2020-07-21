from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(
        upload_to='images', default='/static/images/205607.jpg', blank=True)

    def __str__(self):
        return self.name
