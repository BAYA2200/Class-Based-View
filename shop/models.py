from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.cost}"


class Firm(models.Model):
    name = models.CharField(max_length=50)
    office = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name