from django.db import models
from imagekit import processors
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='blogimg')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)])