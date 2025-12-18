from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    

class DynamicSchema(models.Model):
    name = models.CharField(max_length=100)
    schema = JSONField()
    

class DynamicItem(models.Model): 
    schema_def = models.ForeignKey(DynamicSchema, on_delete=models.PROTECT)
    data = JSONField()