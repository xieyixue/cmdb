#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import os

def hostname():
    sys = os.name
    if sys == 'nt':
        hostname = os.getenv("computername")
        return hostname
    elif sys == "posix":
        from socket import gethostname
        hostname = gethostname()
        return hostname
    else:
        return "UnKwon hostname"


def memory_slot_count():

    #memory插槽数
    sys = os.name
    if sys == "posix":
        count = os.popen2("dmidecode|grep -P -A5 'Memory\s+Device'| grep -v 'Range' | grep -c Size")
        return count
    else:
        return 0
def cpu_slot_count():
    sys = os.name
    if sys == "posix":
        count = os.popen("grep 'physical id' /proc/cpuinfo | sort | uniq | wc -l")
        return count
    else:
        return 0

#print hostname()