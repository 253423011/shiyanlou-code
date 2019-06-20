#!/usr/bin/env python3
import sys
a = set()
for i in range(1,len(sys.argv)):
    a.add(sys.argv[i])
for each_a in a:
    print(each_a,end=' ')

