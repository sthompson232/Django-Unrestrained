from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}: {self.content}'


class FredQueryData(models.Model):
    start_date = models.DateField(max_length=50)
    end_date = models.DateField(max_length=50)
    data_type = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class FilmRatings(models.Model):
    film = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
