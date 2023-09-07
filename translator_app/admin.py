"""This file is used to display models in the Django admin panel."""

from django.contrib import admin
from django.contrib.auth.models import Group
from translator_app.models import Translate

admin.site.unregister(Group)
admin.site.site_header = "Translator"


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    """
    This class will register translate model in admin site.
    """
    list_display = ['from_language', 'to_language']
    list_filter = ['from_language', 'to_language']
    search_fields = ['from_language', 'to_language']
