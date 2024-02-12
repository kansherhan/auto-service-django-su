from django.contrib import admin
from .models import Service, UserServiceCart


class ServiceAdmin(admin.ModelAdmin):
    pass


class UserServiceCartAdmin(admin.ModelAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(UserServiceCart, UserServiceCartAdmin)
