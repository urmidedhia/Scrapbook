from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    msg = models.CharField(max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.name