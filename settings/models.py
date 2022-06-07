from django.db import models

class ClassOfBusiness(models.Model):
    classOfBusiness_text = models.CharField(max_length=200)

class Department(models.Model):
    classOfBusiness = models.ForeignKey(ClassOfBusiness, on_delete=models.CASCADE)
    department_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

