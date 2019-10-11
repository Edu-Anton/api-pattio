from django.db import models

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=50)
  ruc = models.CharField(max_length=11)

class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=8,decimal_places=2)
  company_id= models.ForeignKey(Company,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50)
  product =models.ManyToManyField(Product)

  def __str__(self):
    return self.name
