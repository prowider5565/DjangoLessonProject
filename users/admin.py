from django.contrib import admin

from users.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for User model.
    This can be customized to include additional fields or filters as needed.
    """
    list_display = ('first_name', 'last_name', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    exclude = ('password',)
