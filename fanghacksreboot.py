#!/usr/bin/python3

import urllib.request
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="Reboot camera with fanghacks")
    parser.add_argument("ipaddress", help="The ip address of the camera")
    args = parser.parse_args()
    ipaddress = args.ipaddress
    url = 'http://' + ipaddress + '/cgi-bin/status'
    #url = 'http://' + ipaddress + '/cgi-bin/action?cmd=reboot'
    try:
        urllib.request.urlopen(url)
        success = 'okay'
    except:
        print ('Failed to reset camera')
        success = 'fail'
        pass
    try:
        with open('fanghacksreboot.log', 'a') as f:
            f.write(time.strftime("%Y%m%d%H%M ") + success + '\n')
    except:
        print ('Failed to write logfile')

if __name__ == '__main__':
    main()
