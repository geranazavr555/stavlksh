from django.db import models


class Monitor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Сводный монитор: " + self.name


class CachedHtml(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor",
                              null=False,
                              blank=False)


class MonitoredContest(models.Model):
    stavpoisk_id = models.IntegerField()
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor",
                              null=False,
                              blank=False)

    def __str__(self):
        return "Stavpoisk contest, id " + str(self.stavpoisk_id)


class ExcludedUser(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Monitor,
                              on_delete=models.CASCADE,
                              verbose_name="Monitor",
                              null=False,
                              blank=False)
