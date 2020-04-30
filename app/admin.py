from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Car,
    Owner,
    User,
)


class CarAdmin(admin.ModelAdmin):
    search_fields = ['manufacturer', 'model']
    list_display = ['manufacturer', 'model']
    #exclude = ('model',)

class OwnerAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(User, UserAdmin)
