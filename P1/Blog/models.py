from django.db import models

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField(max_length=200,default='content')
    required = models.BooleanField(default=True)
