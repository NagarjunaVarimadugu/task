from django.db import models

# Create your models here.

class Company(models.Model):

    Name = models.CharField(max_length = 50, default=None)
    Designation = models.CharField(max_length = 50, default=None)
    Position = models.CharField(max_length = 50, default=None)
    Location = models.CharField(max_length = 50, default=None)

    def __str__(self):
        return self.Name