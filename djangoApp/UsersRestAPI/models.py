from django.db import models

# Create your models here.


class UsersOcupation(models.Model):
    ocupation_name = models.CharField(max_length=100)
    ocupation_time = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    
