from django.contrib import admin

from .models import Artifact


@admin.register(Artifact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'shiny']
