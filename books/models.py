from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    author = models.CharField(blank=False, max_length=255)
    version = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.FloatField(blank=False)

    def __str__(self):
        return self.title 

class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.title 