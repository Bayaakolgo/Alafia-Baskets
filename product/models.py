from django.db import models
import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Product(models.Model):
    name = models.CharField(max_length=101, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to=filepath)

    def __str__(self):
        return self.name
