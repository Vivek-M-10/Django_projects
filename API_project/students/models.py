from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.email} - {self.branch}"
