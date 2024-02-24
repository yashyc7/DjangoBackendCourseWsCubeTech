from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class News(models.Model):
    icon=models.ImageField()
    title=models.CharField(max_length=50)
    description=HTMLField()
