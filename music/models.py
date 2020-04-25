from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Musician(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
      return self.name