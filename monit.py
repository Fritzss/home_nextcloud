#!/usr/bin/python3
from subprocess import run
from subprocess import PIPE
from json import loads
from requests import get
from yaml import safe_load

ym = '<your_path_for>docker-compose.yml'
logs = '<your_path_logs>'

def sendTG(bot_message,log):
   log = log
   bot_token = '<your_bot_token>'
   bot_chatID = '<your_chatID>'
   send_text = f'https://123api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
   try:
       response = get(send_text).json()
   except:
       response = get(send_text)
       print(response)
       fmd = open(log, 'a')
       fmd.write(f'{bot_message}\n')
       fmd.close



def getstorage(ym):
    with open(ym, 'r') as file:
       try:
          fyml = safe_load(file)
       except:
          pass

    ymlhdd = fyml["services"]["app"]["volumes"]
    for i in ymlhdd:
        if 'data' in i:
             ymlhdd = i
    ymlhdd = str(ymlhdd).split(':')[0]
    vg = run(['/usr/bin/df', '-h', ymlhdd,'--output=source'], stdout = PIPE )
    vgname = ((vg.stdout.decode('utf-8')).split('/')[-1]).split('-')[0]
    hddraw = run(['/usr/sbin/pvs','-S','vg_name='+vgname ], stdout = PIPE)
    hddraw = (hddraw.stdout.decode('utf-8')).split(' ')
    hdd = ''
    for i in hddraw:
        if 'dev' in i:
              hdd = i
    return hdd, ymlhdd


def getmdadm(raid):
          log = f'{logs}raid.log'
          status = ''
          statusraw = run(['/usr/sbin/mdadm', '-D', raid ], stdout = PIPE, stderr = PIPE, encoding='utf-8')
          for i in str(statusraw.stdout).split('\n'):
                 if 'State' in i and not 'Number' in i:
                        status = i
          if (len(status) == 0):
              status = str(statusraw.stderr)
          if (len(status.split(','))) > 2 or 'clean' not in status:
                     sendTG(f'RAID {status}',log)


def getfree(st):
         log = f'{logs}freeHDD.log'
         free = run(['/usr/bin/df', '-h',st,'--output=pcent' ], stdout = PIPE )
         F = int(free.stdout.decode('utf-8').split('\n')[1].replace('%',''))
         if F < 80:
               sendTG(f'free space {F}%',log)

def getsmart():
         log = f'{logs}smart.log'
         check = "/usr/sbin/smartctl"
         disksraw = run([check, '-j', '--scan'], stdout = PIPE)
         disks = loads(disksraw.stdout)
         for i in disks['devices']:
               diskhealth = run([check, '-j',i['name'], '-H'], stdout = PIPE)
               health = loads(diskhealth.stdout)
               if (health['smart_status']['passed']):
                               sendTG(f"fail {i['name']}",log)


def gettcpu():
          log = f'{logs}tcpu.log'
          tcpuraw = run(['/usr/bin/sensors', '-j'], stdout = PIPE, encoding='utf-8')
          tcpu = loads(tcpuraw.stdout)
          count = 0
          ct = 2
          T = []
          avgT = 0
          for core in tcpu['coretemp-isa-0000']:
                     if 'Adapter' not in core:
                             for t in tcpu['coretemp-isa-0000'][core]:
                                         if 'input' in t:
                                               T.append(tcpu['coretemp-isa-0000'][core][t])
                     try:
                          avgT = sum(T)/len(T)
                     except Exception:
                              pass

          if avgT < 70:
               sendTG(f'T CPU {avgT}C',log)


if __name__ == '__main__':
         storage = getstorage(ym)
         getmdadm(storage[0])
         getfree(storage[1])
         getsmart()
         gettcpu()
