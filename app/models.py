from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk})
