#!/usr/bin/env python3
import sys
a = []
b = []
for i in range(1,len(sys.argv)):
    if (len(sys.argv[i])>=3):
        a.append(sys.argv[i])
    else:

        b.append(sys.argv[i])

for each_a in a:
    print(each_a,end=' ')
print()
for each_b in b:
    print(each_b,end=' ')


