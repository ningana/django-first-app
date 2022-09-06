from django.contrib import admin
from . models import User


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'sexe',
        'role',
        'email',
        'password',
    )

    search_fields = (
        'id',
        'username',
    )

    ordering = (
        'id',
    )


admin.site.register(User, UserAdmin)