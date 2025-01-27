from django.contrib import admin

from . models import(
    Rider, 
    Driver
)


class RiderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'rating',
    ]

class DriverAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'rating',
        'is_available'
    ]

admin.site.register(Rider, RiderAdmin)
admin.site.register(Driver, DriverAdmin)