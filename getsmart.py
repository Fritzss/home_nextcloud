#!/usr/bin/python3
from subprocess import run
from subprocess import PIPE
from json import loads
from requests import get



check = "/usr/sbin/smartctl" 
disksraw = run([check, '-j', '--scan'], stdout = PIPE)
disks = loads(disksraw.stdout)


def sendTG(bot_message):

   bot_token = '1465751773:AAFjgWJTb46Z8swVDJDwMjMSd7GfkUlc3ec'
   bot_chatID = '265801421'
   send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'

   response = get(send_text)

   return response.json()

def getfree():
      free = run(['/usr/bin/df', '-h', '-t', 'xfs', '--output=pcent'], stdout = PIPE )
      F = int(free.stdout.decode('utf-8').split('\n')[1].replace('%',''))
      return F

def getmdadm():
          status = ''
          statusraw = run(['/usr/sbin/mdadm', '-D', '/dev/md/ha:0'], stdout = PIPE, encoding='utf-8')
          for i in str(statusraw.stdout).split('\n'):
                 if 'State' in i and not 'Number' in i:
                        status = i
          return status

def gettcpu():
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
          return avgT





for i in disks['devices']:
         diskhealth = run([check, '-j',i['name'], '-H'], stdout = PIPE)
         health = loads(diskhealth.stdout)
         if not (health['smart_status']['passed']):
                               try:
                                    res = sendTG(f"fail {i['name']}")
                               except:
                                    fsm = open('/var/opt/smart.txt', 'wa')
                                    fsm.write(f"fail {i['name']}\n")
                                    fsm.close

try:
   free = getfree()
   if free > 80:
       try:
          res =  sendTG(f'space used {getfree()}%')
       except:
          ffr = open('/var/opt/freehdd.txt', 'a')
          ffr.write(f'space used {getfree()}%\n')
          ffr.close
except:
    print('fail_getfree')


raidst = getmdadm()
print(len(raidst.split(',')))
#if 'degraded' in raidst or 'resyncing' in raidst:
if (len(raidst.split(','))) > 1:
             try:
                  res = sendTG(f'RAID {raidst}')
             except:
                  fmd = open('/var/opt/mdadm.txt', 'a')
                  fmd.write(f'RAID {raidst}\n') 
                  fmd.close

TCPU = gettcpu()
if TCPU > 70:
            try:
                    res = sendTG(f'Temperatura  {TCPU()}')
            except:
                    ftc = open('/var/opt/TCPU.txt', 'a')
                    ftc.write(f'Temperatura {TCPU}\n')
                    ftc.close

