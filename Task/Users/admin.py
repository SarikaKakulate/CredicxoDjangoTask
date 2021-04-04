from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from Users.models import Student

User = get_user_model()

# Register your models here.


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    fieldsets = (
        ("User info", {
            "fields": ("username", "password",)
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name", "email",)
        }),
        ("Permissions", {
           'fields': ('is_active', 'is_staff', 'is_superuser', 'user_level', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    list_display = ["id", "username", "email", "is_superuser"]
    list_filter = ['user_level', 'is_superuser']
    search_fields = ["username", "email"]
    readonly_fields = []


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "student_class",
        "student_roll",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False