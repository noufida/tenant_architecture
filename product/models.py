from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True