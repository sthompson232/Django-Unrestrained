from django.contrib import admin
from .models import Comment, FredQueryData, FilmRatings

admin.site.register(Comment)
admin.site.register(FredQueryData)
admin.site.register(FilmRatings)