from django.contrib import admin
from .models import AppDetails

@admin.register(AppDetails)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'version', 'description')
    search_fields = ('app_name', 'version')
    list_filter = ('version',)
