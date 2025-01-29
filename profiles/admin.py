from django.contrib import admin

from . models import(
    Rider, 
    Driver,
    Document,
    Vehicle
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

class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        'driver',
        'type',
        'file',
        'is_verified'
    ]

class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'driver',
        'make',
        'model',
        'year'
    ]

admin.site.register(Rider, RiderAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Vehicle, VehicleAdmin)