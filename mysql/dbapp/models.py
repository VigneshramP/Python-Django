from django.db import models

# Create your models here.

class DBDATA(models.Model):
	name = models.CharField(max_length = 50)
	id_card = models.TextField()

class EMPLOYEE(models.Model):
	emp_name = models.CharField(max_length = 50)
	emp_qualification = models.CharField(max_length = 20)
	id_number = models.CharField(max_length = 12)
