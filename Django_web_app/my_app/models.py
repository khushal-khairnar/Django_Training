from django.db import models

# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField()

    # class meta:
    #     db_table="Customer"

    def __str__(self):
        return self.name

class Company(models.Model):
    comp_name=models.CharField(max_length=12)

    def __str__(self):
        return self.comp_name
