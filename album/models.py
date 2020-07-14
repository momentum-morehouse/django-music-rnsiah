from django.db import models

# Create your models here.
class Album(models.Model):
  title = models.CharField(blank=True, null = True, max_length=100)
  date =  models.DateField(auto_now_add=False)
  artistname = models.CharField(blank=True, null = True, max_length=100)
  albumcover = models.ImageField(upload_to='media/album/images/', height_field=None, width_field=None, max_length=None, null=True)


  def __str__(self):
    return f'{self.title}'



class Meta:
  ordering = ['-created']

