from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Categories(MPTTModel):
    name=models.CharField(max_length=100)
    parent=TreeForeignKey('self',on_delete=models.PROTECT,null=True,blank=True,related_name='children')

    class MPTTMeta:
        order_insertion_by=['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    is_digital=models.BooleanField(default=False)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=TreeForeignKey('Categories',on_delete=models.PROTECT)

    def __str__(self):
        return self.name