from django.contrib import admin
# ++++
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation  import gettext_lazy as _
# ++++
from .models import *



class UserAdmin(admin.ModelAdmin):
        fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','is_admin','is_admin2','is_admin3')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User)



admin.site.register(Citoyen)
admin.site.register(Association)
admin.site.register(Evenement)
admin.site.register(Review)
admin.site.register(Alert)
admin.site.register(Evenementnotif)
admin.site.register(Alertnotif)
admin.site.register(dossier)
