from django.http import HttpResponse

from . import scraper


def home(request):
    with open("monitor/cached.html", "r", encoding="utf-8") as file:
        html = "\n".join(file.readlines())
    return HttpResponse(html)
