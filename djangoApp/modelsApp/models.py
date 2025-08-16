from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)