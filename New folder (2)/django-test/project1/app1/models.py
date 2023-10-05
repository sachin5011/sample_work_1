from django.db import models

class appModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()





