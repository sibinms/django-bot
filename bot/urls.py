from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from bot.views import ChatBotView, ChatBotUserListView

urlpatterns = [
    path('webhooks/tutorial/', csrf_exempt(ChatBotView.as_view()), name='chat-bot'),
    path('user/list/', ChatBotUserListView.as_view(), name='user-list')
]
