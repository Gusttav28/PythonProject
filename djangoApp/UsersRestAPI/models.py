from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField

# Create your models here.


class UsersOcupation(models.Model):
    ocupation_name = models.CharField(max_length=100)
    ocupation_time = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    
class DynamicTableForOcupations(models.Model):
    name = models.CharField(max_length=100)
    schema = JSONField()
    

class DynamicItemFortheTable(models.Model):
    table_ref = models.ForeignKey(DynamicTableForOcupations, on_delete=models.CASCADE)
    data = JSONField()