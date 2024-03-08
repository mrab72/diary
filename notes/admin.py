from django.contrib import admin

# Register your models here.
from . import models

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

admin.site.register(models.Note, NoteAdmin)
