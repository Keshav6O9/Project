from django.contrib import admin
import email
from django.db import models
import datetime
import os
def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename ="%s%s", (timeNow,old_filename)
    return os.path.join('uploads/',filename)


# Create your models here.
class newUser(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emailAddress = models.EmailField()
    dateOfBirth = models.DateField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    createPassword = models.CharField(max_length=18,null=True)


admin.site.register(newUser)