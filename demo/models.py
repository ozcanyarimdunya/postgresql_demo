from django.db import models


# Create your models here.
class DemoModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
