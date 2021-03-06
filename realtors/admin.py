from django.contrib import admin

from realtors.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "hire_date")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 5


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)
