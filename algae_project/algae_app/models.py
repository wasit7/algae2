from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

class RawImage(models.Model):
    img = models.ImageField(upload_to='img')
    source = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

class RecallImage(models.Model):
	img = models.ImageField(upload_to='img')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	raw = models.ForeignKey("RawImage", on_delete=models.CASCADE)

class LabelImage(models.Model):
	img = models.ImageField(upload_to='img')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	raw = models.ForeignKey("RawImage", on_delete=models.CASCADE)