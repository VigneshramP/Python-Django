from django.db import models

# Create your models here.
class OverallDefects(models.Model):
	id = models.CharField(primary_key=True, max_length = 15)
	part_defect = models.CharField(max_length = 20)
	observations = models.CharField(max_length = 50)
