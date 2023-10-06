# Create your models here.

from django.db import models
from django.utils import timezone

class Singer(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    debut_year = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    release_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Music(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    album_no = models.SmallIntegerField()
    song_length = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.song
