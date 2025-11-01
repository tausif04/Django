from django.db import models

# Create your models here.
#One to one relationship
class Carcompany(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class CEO(models.Model):
    name=models.CharField(max_length=100)
    carcompany=models.OneToOneField(Carcompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Foreign key --> many-to-one relationship
class CarModel(models.Model):
    name=models.CharField(max_length=100)
    carcompany=models.ForeignKey(Carcompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

#Many to many relationship
class FuelType(models.Model):
    name=models.CharField(max_length=100)
    carmodels=models.ManyToManyField(CarModel)

    def __str__(self):
        return self.name