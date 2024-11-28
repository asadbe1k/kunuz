def check_read_articles(request):
    if "read_articles" not in request.session:
        request.session["read_articles"] = []
    return request.session["read_articles"]
