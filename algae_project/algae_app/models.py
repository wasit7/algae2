from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

class RawImage(models.Model):
    img = models.ImageField(upload_to='img')
    source = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

class RecallImage(models.Model):
	img = models.ImageField(upload_to='img')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	raw = models.ForeignKey("RawImage", on_delete=models.CASCADE)
	algae_pixel=models.IntegerField(default=0)

class Count(models.Model):
	recall = models.ForeignKey("RecallImage", on_delete=models.CASCADE)
	obj_type= models.ForeignKey("ObjType", on_delete=models.CASCADE)
	obj_count = models.IntegerField(default=0)

class ObjType(models.Model):
	description = models.CharField(max_length=20, blank=True, null=True)

class LabelImage(models.Model):
	img = models.ImageField(upload_to='img')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	raw = models.ForeignKey("RawImage", on_delete=models.CASCADE)


