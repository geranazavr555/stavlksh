from django.db import models


class CachedHtml(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)


class MonitoredContest(models.Model):
    stavpoisk_id = models.IntegerField()
