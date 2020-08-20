from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Image(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    
    class Meta:
        ordering = ['order']
