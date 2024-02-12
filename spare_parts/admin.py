from django.contrib import admin
from .models import SparePart, UserSparePartCart


class SparePartAdmin(admin.ModelAdmin):
    pass


class UserSparePartCartAdmin(admin.ModelAdmin):
    pass


admin.site.register(SparePart, SparePartAdmin)
admin.site.register(UserSparePartCart, UserSparePartCartAdmin)
