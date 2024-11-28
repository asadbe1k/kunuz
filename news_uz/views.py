from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import news, Category, Comment, Rating
from .utils import check_read_articles
import re

# Create your views here.


def you(url):

    pattern = r"(?<=v=)[\w-]+"

    match = re.search(pattern, url)
    if match:
        video_id = match.group(0)
        return video_id


def home(request):
    News = news.objects.all().order_by("-pk")[:6]
    Turi = Category.objects.all()
    new = news.objects.all().last()

    video = (
        news.objects.filter(video__isnull=False).exclude(video="").order_by("-pk")[:8]
    )
    cat = Category.objects.all()[:6]
    Newss = news.objects.all().order_by("-pk")[:12]
    Tanlov = news.objects.filter(tanlov=True).order_by("-pk")[:3]

    context = {
        "video": video,
        "news": News,
        "turi": Turi,
        "new": new,
        "cat": cat,
        "newss": Newss,
        "tanlov": Tanlov,
    }
    return render(request, "home.html", context)


def detail(request, pk):
    News = news.objects.get(pk=pk)
    Turi = Category.objects.all()
    cat = Category.objects.all()[:6]
    category = Category.objects.get(id=News.category.id)
    related = news.objects.filter(category=category).order_by("-pk")[:6]
    last_news = news.objects.all().order_by("-pk")[:6]
    News.date_with_offset = News.date + timedelta(hours=5)
    comments = Comment.objects.filter(post=News)
    if News.video:
        News.video = you(News.video)
    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        if all([name, comment]):
            Comment.objects.create(author=name, description=comment, post=News)
            return redirect("detail", pk=pk)

    read_articles = check_read_articles(request)
    if News.id not in read_articles:
        read_articles.append(News.id)
        request.session["read_articles"] = read_articles
        request.session.modified = True
        News.view += 1
        News.save()

    context = {
        "comments": comments,
        "news": News,
        "turi": Turi,
        "cat": cat,
        "related": related,
        "last_news": last_news,
    }
    return render(request, "detail.html", context)


def rating(request, value, pk):
    new = news.objects.get(pk=pk)
    value = int(value)

    rated_articles = request.session.get("rated_articles", [])

    if new.id in rated_articles:
        return redirect("detail", pk=pk)

    if value:
        Rating.objects.create(post=new, value=value)
        rated_articles.append(new.id)
        request.session["rated_articles"] = rated_articles
        request.session.modified = True

    return redirect("detail", pk=pk)


def search(request):
    Turi = Category.objects.all()
    cat = Category.objects.all()[:6]
    last_news = news.objects.all().order_by("-pk")[:6]
    query = request.GET.get("q")
    new = news.objects.all()

    if query:
        neww = new.filter(title__icontains=query)

    context = {
        "turi": Turi,
        "cat": cat,
        "news": neww,
        "newss": last_news,
    }
    return render(request, "list.html", context)


def category(request):
    Turi = Category.objects.all()
    cat = Category.objects.all()[:6]
    catid = request.GET.get("category")
    last_news = news.objects.all().order_by("-pk")[:6]
    News = news.objects.filter(category=catid).order_by("-pk")[:12]

    context = {
        "news": News,
        "turi": Turi,
        "cat": cat,
        "newss": last_news,
    }
    return render(request, "category.html", context)


def tags(request):
    Turi = Category.objects.all()
    cat = Category.objects.all()[:6]
    tags = request.GET.get("tag")
    new = news.objects.filter(tag=tags)
    last_news = news.objects.all().order_by("-pk")[:6]

    context = {
        "new": new,
        "turi": Turi,
        "cat": cat,
        "newss": last_news,
    }
    return render(request, "tags.html", context)
