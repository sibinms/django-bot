from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from bot.models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_user_id', 'joke', 'count')


admin.site.unregister(User)
admin.site.unregister(Group)
