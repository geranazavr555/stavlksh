from django.db import models


class Monitor(models.Model):
    name = models.CharField(max_length=255)


class CachedHtml(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor")


class MonitoredContest(models.Model):
    stavpoisk_id = models.IntegerField()
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor")


class ExcludedUser(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor")
