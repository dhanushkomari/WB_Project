from django.contrib import admin
from .models import  Restaurant, Bot, VBSettings, MobileSettings, HandSettings
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['rest_name', 'rest_location']
admin.site.register(Restaurant, RestaurantAdmin)

class BotAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['rest', 'bot_name', 'bot_color', 'bot_no', 'avialable']
admin.site.register(Bot, BotAdmin)

class VBSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'time']
    list_per_page = 20
admin.site.register(VBSettings, VBSettingsAdmin)

class MobileSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','bot_name', 'mob_no', 'speaker', 'time']
    list_per_page = 20
admin.site.register(MobileSettings, MobileSettingsAdmin)

class HandSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'bot_name', 'username']
    list_per_page = 20
admin.site.register(HandSettings, HandSettingsAdmin)
