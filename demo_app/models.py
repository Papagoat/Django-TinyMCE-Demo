from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Demo(models.Model):
    demo_title = models.CharField(max_length=200)
    demo_textfield = HTMLField()
