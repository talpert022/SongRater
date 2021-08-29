from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Songs(models.Model):
    song = models.CharField(max_length=50, primary_key=True)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.song


class Ratings(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return_string = str(self.song) + " - " + str(self.username)
        return return_string


class Years(models.Model):
    year = models.IntegerField(default=2000)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    president = models.CharField(max_length=50)

    def __str__(self):
        return str(self.year) + " - " + str(self.president) + " - " + str(self.song)
