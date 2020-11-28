#!/usr/bin/python3
from subprocess import run
from subprocess import PIPE
from requests import get
from glob import glob

def sendTG(bot_message):
       bot_token = '<your_bot_token>'
       bot_chatID = '<your_chatID>'
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

def send(check):
    folder = '<your_path_logs>/*'
    if check:
        F = glob(folder)
        for f in F:
             print(f)
             if len(f) > 0:
                 try:
                      sendTG(f"{ch(f)}")
                      f = open(f, 'w')
                      f.write('')
                      f.close()
                 except Exception:
                       pass


if __name__ == '__main__':
      check = ping_ip('api.telegram.org')
      send(check)