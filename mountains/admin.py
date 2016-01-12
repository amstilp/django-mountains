from django.contrib import admin
from . models import Mountain, MountainRange

class MountainAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'mountain_range')

# Register your models here.
admin.site.register(Mountain, MountainAdmin)
admin.site.register(MountainRange)