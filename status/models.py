from django.db import models
import datetime
from django.core.validators import RegexValidator

class Applicant(models.Model):
	name = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email_address = models.EmailField()
	driver_license_number = models.CharField("Driver license number",max_length=10, primary_key=True)
	def __str__(self):
		return self.driver_license_number
	
class CourtRecord(models.Model):
	court_record_number = models.IntegerField()
	def __str__(self):
		return str(self.court_record_number)
	status = models.CharField(max_length=20)
	notes = models.CharField(max_length=2000, blank=True)
	driver_license_number = models.ForeignKey(Applicant, on_delete=models.CASCADE)
