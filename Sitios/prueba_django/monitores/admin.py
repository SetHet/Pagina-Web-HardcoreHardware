from django.contrib import admin
from .models import Monitor
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Monitor,UserAdmin)
