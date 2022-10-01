from django.db import models

class Login (models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(("password"), max_length=50)
