from distutils.command.upload import upload
from email.mime import image
from django.db import models


# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    # image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
 
    
    def __str__(self):
        return self.title