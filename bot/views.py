import json

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView

from bot.utils import jokes, send_message
from bot.models import BotUser


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
from common.constant import BOT_WELCOME_MESSAGE


class ChatBotView(View):
    """
    Telegram chat bot view for webhook
    """

    def post(self, request, *args, **kwargs):
        telegram_data = json.loads(request.body)
        print(telegram_data)
        try:
            telegram_call_back = telegram_data['callback_query']['data']
            telegram_user = telegram_data['callback_query']['from']['id']
            telegram_user_name = telegram_data['callback_query']['from']['first_name']
            bot_user, _ = BotUser.objects.get_or_create(telegram_user_id=telegram_user,
                                                        name=telegram_user_name, joke=telegram_call_back)
        except (KeyError, ValueError) as e:
            telegram_call_back = None
        if telegram_call_back:
            msg = jokes(telegram_call_back)
            bot_user.count = bot_user.count + 1
            bot_user.save()
            send_message(msg, telegram_user)
        telegram_message = telegram_data.get('message', None)
        if telegram_message:
            telegram_chat_room = telegram_message.get('chat')
            telegram_room_id = telegram_chat_room.get('id')
            telegram_chat = telegram_message.get('text')
            msg = BOT_WELCOME_MESSAGE
            send_message(msg, telegram_room_id)
        return JsonResponse({"ok": "POST request processed"})


class ChatBotUserListView(ListView):
    """
    Chat bot users listing View
    """
    template_name = "bot/bot_user_list.html"
    model = BotUser
    context_object_name = 'users'
    ordering = 'count'

