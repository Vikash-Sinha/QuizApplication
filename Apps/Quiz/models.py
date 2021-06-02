from django.db import models

# Create your models here.
class Quizs(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    gender = models.CharField(max_length=50,blank=True, null=True)
    issue = models.CharField(max_length=500,blank=True, null=True)
    img = models.ImageField(upload_to='issue/', null=True, blank=True)


class Domains(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    sudomain = models.CharField(max_length=200,blank=True, null=True)
