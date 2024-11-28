from django.contrib import admin
from .models import news, Category, Location, Tags, Comment, Rating

# Register your models here.
admin.site.register(news)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Rating)
