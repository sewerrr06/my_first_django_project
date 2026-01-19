from django.db import models

# Create your models here.
class Phone(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField(max_length=800, blank=True, null=True)
    reviews = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.model} - {self.price}'

class Laptop(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField(max_length=800, blank=True, null=True)


    def __str__(self):
        return f'{self.name} {self.model} - {self.price}'