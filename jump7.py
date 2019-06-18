#!/usr/bin/env python3
for i in range(1,101):
	if (i%7==0):
		continue
	if (i>=70 and i<=79):
		continue
	if (i%10==7):
		continue
	print(i)

