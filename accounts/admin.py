from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'date_joined', 'last_login', 'is_active', 'is_staff',)
    search_fields = ('phone_number',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    ordering = ('phone_number',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )

admin.site.register(Users, CustomUserAdmin)



