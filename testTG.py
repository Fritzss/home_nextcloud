#!/usr/bin/python3
from requests import get


def sendTG(bot_message):
          bot_token = '<your_bot_TG>'
          bot_chatID = '<your_chatID>'
          send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"
          response = get(send_text)
          return response.json()
print(sendTG('test_message'))
