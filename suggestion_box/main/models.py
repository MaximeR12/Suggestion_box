from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    
class IdeaCreationForm(forms.Form):
    name = forms.CharField(max_length=100)
    details = forms.CharField(max_length=200)