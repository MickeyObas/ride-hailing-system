from django.contrib import admin

from .models import (
    User
)

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'phone_number',
        'first_name',
        'last_name',
        'status',
        'deleted_at',
        'created_at',
        'updated_at',
    ]

admin.site.register(User, UserAdmin)