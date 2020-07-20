from django.db import models

# Create your models here.
class Album(models.Model):
  title = models.CharField(blank=True, null = True, max_length=100)
  artistname = models.CharField(blank=True, null = True, max_length=100)
  albumcover = models.TextField( null=True, blank=True)
  date= models.DateField()


  def __str__(self):
    return f'{self.title}'



class Meta:
  ordering = ['-created']

