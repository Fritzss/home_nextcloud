#!/usr/bin/python3
from subprocess import run
from subprocess import PIPE
from requests import get
from glob import glob

def sendTG(bot_message):

   bot_token = '1465751773:AAFjgWJTb46Z8swVDJDwMjMSd7GfkUlc3ec'
   bot_chatID = '265801421'
   send_text =  f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
   response = get(send_text)
   return response.json()


def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = run(['ping', '-c', '3', '-n', ip_address],
                           stdout=PIPE,
                           stderr=PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True #, reply.stdout
    else:
        return False #, reply.stderr


def ch(f):
       f1 = ""
       with open(f) as file:
            f1 = file.readlines()
       return f1


if ping_ip('api.telegram.org'):
        folder = '/var/opt/*txt'
        F = glob(folder)
        for f in F:
             if len(f)>0:
                 try:
                      sendTG(f"{ch(f)}")
                      f = open(f, 'w')
                      f.write('')
                      f.close()
                 except Exception:
                       pass

