from django.contrib import admin

from . import models

class MonitorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(models.Monitor, MonitorAdmin)


class CachedHtmlAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "date", "owner")


admin.site.register(models.CachedHtml, CachedHtmlAdmin)


class MonitoredContestAdmin(admin.ModelAdmin):
    list_display = ("stavpoisk_id", "owner")


admin.site.register(models.MonitoredContest, MonitoredContestAdmin)


class ExcludedUserAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


admin.site.register(models.ExcludedUser, ExcludedUserAdmin)
