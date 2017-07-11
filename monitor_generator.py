from time import sleep
import os

import django
from django.template.loader import render_to_string

from monitor import scraper


def generate(*args):
    contests, contestants = scraper.get_summary_results(*args)
    context = {"contestants": contestants, "contests": contests}
    html = render_to_string("monitor/summary_monitor.html", context)

    from monitor import models
    models.CachedHtml.objects.all().delete()
    models.CachedHtml(content=html).save()


def run_loop(*args):
    while True:
        print("Monitor generating started")
        generate(*args)
        print("Monitor generating finished")
        sleep(60)

if __name__ == "__main__":
    print("Started preparing instance of Django for worker")
    os.environ["DJANGO_SETTINGS_MODULE"] = "stavlksh.settings"
    django.setup()
    print("Preparing finished")
    run_loop(134, 135)
