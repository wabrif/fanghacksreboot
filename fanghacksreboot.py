#!/usr/bin/python3

import urllib.request
import time

urllib.request.urlopen('http://192.168.1.20/cgi-bin/action?cmd=reboot')
with open('fanghacksreboot.log', 'a') as f:
    f.write(time.strftime("%Y%m%d%H%M") + '\n')
