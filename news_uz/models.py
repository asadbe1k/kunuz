from django.db import models
from ckeditor.fields import RichTextField
import uuid


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=101)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=101)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=111)
    slug = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class news(models.Model):
    title = models.CharField(max_length=111)
    image = models.ImageField()
    description = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    tanlov = models.BooleanField(blank=True)
    video = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tags)
    view = models.IntegerField(blank=True, default=0)

    def avg_rating(self):
        rating_count = self.ratings.all().count()
        if rating_count == 0:
            return 0
        sum_ratings = sum(rating.value for rating in self.ratings.all())
        return sum_ratings / rating_count

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=155)
    description = models.TextField()
    post = models.ForeignKey(news, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(news, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"{str(self.value)} stars for {self.post} "
