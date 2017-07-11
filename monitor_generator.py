from time import sleep
import os

import django
from django.template.loader import render_to_string

from monitor import scraper


def generate(*args):
    contests, contestants = scraper.get_summary_results(*args)
    context = {"contestants": contestants, "contests": contests}
    html = render_to_string("monitor/summary_monitor.html", context)
    with open("monitor/cached.html", "w", encoding="utf-8") as file:
        file.write(html)


def run_loop(*args):
    print("test_run_loop")
    generate(*args)
    print("test_run_loop2")
    sleep(60)

if __name__ == "__main__":
    print("test1")
    os.environ["DJANGO_SETTINGS_MODULE"] = "stavlksh.settings"
    print("test2")
    django.setup()
    run_loop(134, 135)
