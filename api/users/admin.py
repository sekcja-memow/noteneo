from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User
from users.forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    ordering = ('email',)
    list_display = ('email', 'name',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'address', 'image',)
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'name', 'address', 'image', 'password1', 'password2', 'is_staff', 'is_active',
            )
        }
        ),
    )
    search_fields = ('email', 'address', 'first_name', 'last_name',)
