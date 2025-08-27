from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, UserProfile


class UserProfileInline(admin.StackedInline):
    """Inline profile editor in user admin"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    extra = 0


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    """Custom admin panel for CustomUser"""

    # Fields to display in the list view
    list_display = ("email", "role", "is_active", "is_staff", "is_superuser", "date_joined")
    list_filter = ("role", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "profile__first_name", "profile__last_name")

    ordering = ("-date_joined",)

    # Fields shown in the user detail/edit page
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("role", "department")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Fields used when creating a new user in admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "role", "is_active", "is_staff", "is_superuser"),
        }),
    )

    inlines = [UserProfileInline]

    # So profile fields can be searched directly
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin panel for UserProfile separately (optional)"""
    list_display = ("full_name", "user", "phone_number", "city", "country", "created_at")
    search_fields = ("first_name", "last_name", "user__email", "phone_number", "city", "country")
    list_filter = ("city", "country", "created_at")
