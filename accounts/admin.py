# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_active',
                    'is_staff')
    search_fields = ('email', 'username')
    ordering = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    list_filter = ('is_active', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
