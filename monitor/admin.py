from django.contrib import admin

from . import models


class CachedHtmlAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "date")

admin.site.register(models.CachedHtml, CachedHtmlAdmin)


class MonitoredContestAdmin(admin.ModelAdmin):
    list_display = ("stavpoisk_id", )

admin.site.register(models.MonitoredContest, MonitoredContestAdmin)


class ExcludedUserAdmin(admin.ModelAdmin):
    list_display = ("name", )

admin.site.register(models.ExcludedUser, ExcludedUserAdmin)
