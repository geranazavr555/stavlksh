from datetime import datetime
from django.shortcuts import render

from . import scraper


class Cache:
    def __init__(self, function_to_get_data, time_to_live):
        self.func = function_to_get_data
        self.date = datetime.min
        self.ttl = time_to_live
        self.data = None

    def __call__(self, *args, **kwargs):
        if (datetime.now() - self.date).total_seconds() > self.ttl or (self.data is None):
            self.data = self.func(*args, **kwargs)
            self.date = datetime.now()
        return self.data

get_summary_results = Cache(scraper.get_summary_results, 60)


def home(request):
    contests, contestants = get_summary_results(134)
    context = {"contestants": contestants, "contests": contests}
    return render(request, "monitor/summary_monitor.html", context)
