from django.db import models

# Create your models here.

class CvPhotoModel(models.Model):
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.photo.name

class PhotoModel(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.image.name

class ResumeModel(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name
    
    
