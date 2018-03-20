from django.db import models
import os





class Complaint(models.Model):

    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=400)
    location = models.CharField(max_length = 100)

    
    # lat = models.FloatField()
    # lon = models.FloatField()

    pic = models.ImageField(upload_to='img')

    date_published = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title
