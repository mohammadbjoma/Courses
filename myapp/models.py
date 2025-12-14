from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    hours = models.CharField(max_length=255)
    student = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
