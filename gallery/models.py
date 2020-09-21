from django.db import models

# Create your models here.


class gallery(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery')
    desc = models.TextField()

    def __str__(self):
    	return self.name
