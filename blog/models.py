from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class post1(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()