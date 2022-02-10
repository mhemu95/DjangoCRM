from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name