from django.shortcuts import render

from . import cacher
from . import scraper


get_summary_results_cached = cacher.cache
get_summary_results_cached.set_function(scraper.get_summary_results)
get_summary_results_cached.set_args(134, 135)


def home(request):
    contests, contestants = get_summary_results_cached()
    context = {"contestants": contestants, "contests": contests}
    return render(request, "monitor/summary_monitor.html", context)
