import os
from django.db import models

# Create your models here.
class Observer(models.Model):
	name = models.CharField(max_length = 100)
	startTime = models.DateTimeField(null = True, name = 'evaluation_started')
	endTime = models.DateTimeField(null = True, name = 'evaluation_ended')

	def __str__(self):
		return str(self.name)

class Image(models.Model):
	scene = models.IntegerField(default = 0)
	image_file = models.ImageField(default = 'Null', upload_to = 'images')
	reference = models.BooleanField(default = False)
	hidden_reference = models.BooleanField(default = False)

	def __str__(self):
		return os.path.basename(getattr(self.image_file, 'name'))

class Rating(models.Model):
	observer = models.ForeignKey(Observer, on_delete = models.CASCADE)
	image = models.ForeignKey(Image, on_delete = models.CASCADE)
	dateTime = models.DateTimeField(blank = True, name = 'date_rated')
	score = models.IntegerField(default = 0)