import json
import random

import requests

from django_bot.settings import TELEGRAM_URL, BOT_TOKEN


def jokes(keyword):
    """
    function for generating random jokes, currently its uses static jokes
    :param keyword:
    :return:
    """
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, 
                break it up!" """],
        'dumb': ["""THis is dump joke , like you ):""",
                 """Yaa I am just joking like a dump"""]
    }
    if keyword == 'fat':
        return random.choice(jokes['fat'])
    elif keyword == 'stupid':
        return random.choice(jokes['stupid'])
    elif keyword == 'dumb':
        return random.choice(jokes['dumb'])
    else:
        return "Tell me fat,stupid or dumb"


def send_message(message, chat_id):
    """
    function basically sends message to the bot user
    :param message:
    :param chat_id:
    :return:
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "chat_id": chat_id,
        "text": message,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Fat",
                        "callback_data": "fat",
                    }
                ],
                [
                    {
                        "text": "Dumb",
                        "callback_data": "dumb",
                    }
                ],
                [
                    {
                        "text": "Stupid",
                        "callback_data": "stupid",
                    }
                ]
            ]
        }
    }
    data = json.dumps(data)
    response = requests.post(
        f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", headers=headers, data=data
    )
