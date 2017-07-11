from django.http import HttpResponse

from . import scraper
from . import models


def home(request):
    html = models.CachedHtml.objects.all()[0]
    html = html.content
    return HttpResponse(html)
