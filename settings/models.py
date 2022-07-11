from django.db import models

class ClassOfBusiness(models.Model):
    classOfBusiness_text = models.CharField(max_length=200)
    def __str__(self):
        return self.classOfBusiness_text

class Department(models.Model):
    classOfBusiness = models.ForeignKey(ClassOfBusiness, on_delete=models.CASCADE, blank=True, null=True)
    department_text = models.CharField(max_length=200)
    def __str__(self):
        return self.department_text

