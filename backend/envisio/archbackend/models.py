from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username}, {self.firstname} {self.lastname}"