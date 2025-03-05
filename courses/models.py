from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.title} - {self.language}'
