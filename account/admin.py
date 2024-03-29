from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserModelAdmin


class UserModelAdmin(BaseUserModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "mobile", "userName", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["mobile", "userName"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "mobile", "userName", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id", "created"]
    filter_horizontal = []


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
