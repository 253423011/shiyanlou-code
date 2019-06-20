#!/usr/bin/env python3
import sys
a = dict()
for i in range(1,len(sys.argv)):
    str1 = sys.argv[i]
    b, c = str1.split(':')
    a[b] = c
for key,value in a.items():
    print('ID:{} Name:{}'.format(key,value))

