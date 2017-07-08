from django.shortcuts import render

from . import scraper


def home(request):
    contests, contestants = scraper.get_summary_results(91, 94, 96, 98, 101, 103, 105, 107, 109, 112, 113, 116)
    context = {"contestants": contestants, "contests": contests}
    return render(request, "monitor/summary_monitor.html", context)
