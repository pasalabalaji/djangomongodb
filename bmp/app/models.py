from django.db import models

# Create your models here.

class department(models.Model):
      deptId=models.CharField(max_length=10)
      deptName=models.CharField(max_length=100)

class employee(models.Model):
      empId=models.CharField(max_length=10)
      empName=models.CharField(max_length=100)
      empDept=models.CharField(max_length=10)
      empJoinDate=models.DateField()
      empPhoto=models.ImageField()