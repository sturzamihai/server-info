#   last updated: 06.04.2018. v0.1.2
#   
#   developed by: mihai sturza.
#   ~ simple tool for determining useful information about the server you connected to. ~
#   ? will work on most python versions. ?

#imports
from __future__ import print_function
from collections import OrderedDict
import json, os, platform, subprocess, sys, getpass
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# class for stylized printing
"""
class tcolors:
    DEFAULT = '\033[39m'
    RED = '\033[91m'
    WARNING = '\033[93m'    # will use those later
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
"""

ipshow = False

def check_args():
    for args in sys.argv:
        if(args == '-h' or args == "--help"):
            print_help()
            sys.exit()
        elif(args == '-ip'):
            global ipshow
            ipshow = True


def print_help():
    print("Optional arguments:\n")
    print("-h, --help: Shows this dialog and kills the program.")
    print("-ip: Shows the machine's public IP in the 'Connection' section.")

def print_ip_info():
    # internet connection
    try:
        ipinfo = json.loads(urlopen("http://ipinfo.io/json").read().decode('utf-8'))
        if ipshow == True:
            print("[*] IP: {}".format(ipinfo['ip']))
        print("[*] COUNTRY: {0}\n[*] CITY: {1}\n[*] ORG: {2}".format(ipinfo['country'],ipinfo['city'],ipinfo['org']))
    except:
        print("[*] You are not connected to the internet.")

def print_sudo_access():
    # 'super-user do' acces
    if os.getuid() or getpass.getuser()=="root":
        print("[*] SUDO: YES")
    else:
        print("[*] SUDO: NO")

def print_specs():
    # os info
    distro = platform.linux_distribution()
    print("[*] OS: {}".format(platform.system()))
    print("[*] Distribution: {0} {1} ({2})".format(distro[0],distro[1],distro[2]))
    cpu = get_processor_info()
    print("[*] CPU: {}".format(cpu))
    ram = get_ram_info()
    print("[*] RAM: {}".format(ram))

def ram_info():
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

def get_ram_info():
    raminfo = ram_info()
    return raminfo['MemTotal']

def processor_info():
    cpuinfo=OrderedDict()
    procinfo=OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs = nprocs + 1
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return cpuinfo

def get_processor_info():
    cpuinfo = processor_info()
    num = 0
    for processor in cpuinfo.keys():
        num = num + 1
    for processor in cpuinfo.keys():
        return "{0}x {1}".format(num,cpuinfo[processor]['model name'])

if __name__ == "__main__":
    check_args()
    print(" -- Permissions")
    print_sudo_access()
    print(' -- Machine Info')
    print_specs()
    print(" -- Connection")
    print_ip_info()