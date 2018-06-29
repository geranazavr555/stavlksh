from time import sleep
import os

import django
from django.template.loader import render_to_string
from requests.exceptions import ConnectionError

from monitor import scraper


def generate_all():
    active_monitors = models.Monitor.objects.filter(active=True)
    for monitor in active_monitors:
        generate(monitor)


def generate(monitor):
    args = (contest.stavpoisk_id for contest in models.MonitoredContest.objects.filter(owner__id=monitor.id))

    excluded_contestants = list(user.name for user in models.ExcludedUser.objects.filter(owner__id=monitor.id))

    contests, contestants = scraper.get_summary_results(*args)

    tmp_contestants = []
    for contestant in contestants:
        if contestant[0] not in excluded_contestants:
            tmp_contestants.append(contestant)
    contestants = tmp_contestants

    context = {"contestants": contestants, "contests": contests}
    html = render_to_string("monitor/summary_monitor.html", context)

    cached_html, created = models.CachedHtml.objects.get_or_create(defaults={"owner": monitor}, owner__id=monitor.id)
    cached_html.content = html
    cached_html.save()


def run_loop():
    while True:
        print("Monitor generating started")
        try:
            generate_all()
        except ConnectionError:
            print("Can't generate monitor -- Connecting Error")
        else:
            print("Monitor generating finished")
        sleep(55)


if __name__ == "__main__":
    print("Started preparing instance of Django for worker")
    os.environ["DJANGO_SETTINGS_MODULE"] = "stavlksh.settings"
    django.setup()
    from monitor import models
    print("Preparing finished")

    run_loop()
