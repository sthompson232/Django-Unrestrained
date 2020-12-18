from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content