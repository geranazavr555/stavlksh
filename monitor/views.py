from django.http import HttpResponse, HttpResponseBadRequest

from . import scraper
from . import models


def exact_monitor(request, monitor_id):
    try:
        html = models.CachedHtml.objects.get(id=int(monitor_id)).content
        return HttpResponse(html)
    except models.CachedHtml.DoesNotExist:
        return HttpResponseBadRequest("No such monitor: id = " + monitor_id)