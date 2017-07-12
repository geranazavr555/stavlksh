from time import sleep
import os

import django
from django.template.loader import render_to_string
from requests.exceptions import ConnectionError

from monitor import scraper


def generate():
    args = (contest.stavpoisk_id for contest in models.MonitoredContest.objects.all())

    contests, contestants = scraper.get_summary_results(*args)
    context = {"contestants": contestants, "contests": contests}
    html = render_to_string("monitor/summary_monitor.html", context)

    models.CachedHtml.objects.all().delete()
    models.CachedHtml(content=html).save()


def run_loop():
    while True:
        print("Monitor generating started")
        try:
            generate()
        except ConnectionError:
            print("Can't generate monitor")
        else:
            print("Monitor generating finished")
        sleep(5)

if __name__ == "__main__":
    print("Started preparing instance of Django for worker")
    os.environ["DJANGO_SETTINGS_MODULE"] = "stavlksh.settings"
    django.setup()
    from monitor import models
    print("Preparing finished")

    run_loop()
