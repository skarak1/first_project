from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
	
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=264,null=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE,null=True)
    date = models.DateField(default=timezone.now())
    def __str__(self):
        return str(self.date)


#python manage.py migrate
#python manage.py makemigrations first_app