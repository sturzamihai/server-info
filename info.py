# Author: Sturza Mihai
# Depedencies: None - all come installed with python
# Version: 0.2.1 - Updated 2018-02-11 16:15:14

import os, sys, json, socket, getpass, threading, datetime, platform, urllib.request, subprocess

def portConnect(port:int, delay:int, output:list):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(delay)
    try:
        sock.connect(('127.0.0.1',port))
        output[port] = True
    except:
        output[port] = False

def ipData():
    ipjson = json.loads(urllib.request.urlopen("http://ipinfo.io/json").read().decode('utf-8'))

    print("\033[91mIP: \033[93m{0}\n\033[91mCountry: \033[93m{1}\n\033[91mISP: \033[93m{2}\n".format(str(ipjson['ip']),str(ipjson['country']),str(ipjson['org'])))


def portData():

    threads = []
    output = {}
    openPorts = 0

    for i in range(65530):
        t = threading.Thread(target=portConnect,args=(i,1,output))
        threads.append(t)

    for i in range(65530):
        threads[i].start()

    for i in range(65530):
        threads[i].join()

    for i in range(65530):
        if output[i] == True:
            print("\033[91mPort: \033[93m{0} \033[91m(OPEN)\n".format(i))
            openPorts += 1
    print("\033[91mOpen Ports: \033[93m{}\n".format(openPorts))



def osData():
    print("\033[91mUsername: \033[93m{0}\n\033[91mProcessor: \033[93m{1}\n\033[91mArchitecture: \033[93m{2}\n\033[91mLinux Distro: \033[93m{3}\n\033[91mNetwork Node: \033[93m{4}\n\033[91mSystem Time: \033[93m{5}\n".format(getpass.getuser(),platform.processor(),platform.machine(),platform.linux_distribution(),platform.node(),datetime.datetime.now()))

def timeData():
    raw = subprocess.check_output('uptime').decode('utf-8').replace(',','')
    days = int(raw.split()[2])
    if 'min' in raw:
    	hours = 0
    	minutes = int(raw[4])
    else:
    	hours, minutes = map(int,raw.split()[4].split(':'))
    print("\033[91mUp-time: \033[93m{0} days, {1} hours,{2} minutes\n".format(days,hours,minutes))
if __name__ == "__main__":
    print("\033[92m===HOST-INFO===\n")
    try:
        osData()
        timeData()
        print("\033[92m===NETWORK-INFO===\n")
    except:
        print("\033[91mCould not retrive OS Data.\n")
        print("\033[92m===NETWORK-INFO===\n")
    try:
        ipData()
        portData()
    except:
        print("\033[91mCould not retrive Network Data.\n")
