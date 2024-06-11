from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (None, {"fields": ("email", "password","username")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "full_name",
                    "address",
                    "phone",
                    "description",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "full_name",
        "address",
        "phone",
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups","full_name")

    search_fields = (
        "email",
        "full_name",
        "address",
        "phone",
    )
    ordering = ("email",)


# Register the new CustomUserAdmin
admin.site.register(User, CustomUserAdmin)