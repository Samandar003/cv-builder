from django.db import models
import os
import random
# Create your models here.


class CvPhotoModel(models.Model):
    photo = models.ImageField(upload_to='photos/')
    # name = models.CharField(max_length=500)
    # address = models.CharField(max_length=500)
    # phone = models.CharField(max_length=500)
    # email = models.EmailField()
    # telegram = models.CharField(max_length=500)
    # github = models.CharField(max_length=500)
    # linkedin = models.CharField(max_length=500)
    # website = models.CharField(max_length=500)
    # edu_place = models.CharField(max_length=500)
    # course = models.CharField(max_length=500)
    # starting_date = models.CharField(max_length=500)
    # ending_date = models.CharField(max_length=500)
    # job_role = models.CharField(max_length=500)
    # work_place = models.CharField(max_length=500)
    # start_date = models.CharField(max_length=500)
    # end_date = models.CharField(max_length=500)
    # job_desc = models.CharField(max_length=500)
    # skills = models.CharField(max_length=500)
    # project1 = models.CharField(max_length=500)
    # project2 = models.CharField(max_length=500)
    # project3 = models.CharField(max_length=500, null=True, blank=True)
    # project4 = models.CharField(max_length=500, null=True, blank=True)
    # certificate1 = models.CharField(max_length=500)
    # certificate2 = models.CharField(null=True, blank=True, max_length=500)


    def __str__(self):
        return self.photo.name
    
class ResumeModel(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name
    
class SampleResumeModel(models.Model):
    file = models.FileField(upload_to='sample/') 


