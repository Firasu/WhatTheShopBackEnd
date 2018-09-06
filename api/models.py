from django.db import models
from django.contrib.auth.models import User

class Expert(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    profession = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    photo = models.FileField(null=True, blank=True)
    description = models.TextField()
    website = models.URLField(max_length=200)
    years_experience = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Item(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    photo = models.FileField(null=True, blank=True)
    price = models.DecimalField(max_digits=200, decimal_places=3)


    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item, through="OrderItem")
#
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
#
