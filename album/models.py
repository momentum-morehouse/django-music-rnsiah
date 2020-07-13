from django.db import models

# Create your models here.
class Album(models.Model):
  title = models.CharField(blank=True, null = True, max_length=100)
  date =  models.DateTimeField(auto_now_add=False)
  artistname = models.CharField(blank=True, null = True, max_length=100)

class Meta:
  ordering = ['-created']

