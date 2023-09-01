from django.contrib import admin
from .models import TelegramUsers,Subscriptions

@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    list_display=("id","nickname","user_id","phone")




@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display=("id","user","date","is_active")