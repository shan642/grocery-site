from django.db import models

# Create your models here.
class user(models.Model):
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    

class product(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=500)
    price=models.PositiveIntegerField(default=0)
    stock=models.PositiveIntegerField(default=0)
    img=models.ImageField(upload_to="uploads/")
    def __str__(self):
        return self.name

class cart(models.Model):
    item=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.name


    