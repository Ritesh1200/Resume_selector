from django.db import models

# Create your models here.

def content_file_name(instance, filename):
    filename = instance.username + filename
    return '/'.join([filename])
class Resume(models.Model):
    username = models.CharField(max_length=100)
    resume = models.FileField(upload_to=content_file_name, null=False)
    