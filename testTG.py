#!/usr/bin/python3
from requests import get


def sendTG(bot_message):
          bot_token = '1465751773:AAFjgWJTb46Z8swVDJDwMjMSd7GfkUlc3ec'
          bot_chatID = '265801421'
          send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"
          response = get(send_text)
          return response.json()


print(sendTG('asdgffgd'))
