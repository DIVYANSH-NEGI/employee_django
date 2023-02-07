from django.db import models

# Create your models here.



class Company(models.Model):
        Company_id=models.BigAutoField(primary_key=True)
        Domain = models.CharField(max_length=100)
        address = models.CharField(max_length=250)
        email = models.EmailField(max_length=100)

        def __str__(self): return self.Domain



class Employee(models.Model):
    Emp_id =models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    position = models.CharField(max_length=100)
    Company_id=models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self): return self.name
