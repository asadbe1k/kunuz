from django.urls import path
from .views import home, detail, rating, search, category, tags

urlpatterns = [
    path("", home, name="home"),
    path("detail/<int:pk>/", detail, name="detail"),
    path("rating/<value>/<int:pk>", rating, name="rating"),
    path("search/", search, name="search"),
    path("category/", category, name="category"),
    path("tags/", tags, name="tags"),
]
