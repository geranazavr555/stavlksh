from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from . import scraper
from . import models


def exact_monitor(request, monitor_id):
    try:
        html = models.CachedHtml.objects.get(owner_id=int(monitor_id)).content
        return HttpResponse(html)
    except models.CachedHtml.DoesNotExist:
        return HttpResponseBadRequest("No such monitor: id = " + monitor_id)


def home(request):
    return render(request, "monitor/landing.html", {"monitors" : models.Monitor.objects.all()})