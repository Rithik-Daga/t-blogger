from . import models
from django.contrib import admin


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "date_created"]
    list_filter = ["author", "date_created"]
    ordering = ["id"]
    list_per_page = 50


# Register your models here.
admin.site.register(models.Blog, BlogAdmin)
