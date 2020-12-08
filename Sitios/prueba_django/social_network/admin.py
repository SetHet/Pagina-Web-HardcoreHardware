from django.contrib import admin
from .models import SocialNetwork

# Register your models here.
class SocialNetworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(SocialNetwork, SocialNetworkAdmin)