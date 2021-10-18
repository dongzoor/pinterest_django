from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)