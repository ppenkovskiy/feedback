from django.db import models


# This model only stores the path to the file on the hard drive
class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')

