from django.contrib import admin

from . import models


class CachedHtmlAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "date")

admin.site.register(models.CachedHtml, CachedHtmlAdmin)
