#!/usr/bin/env python
#
# Sample code to read in test cases:
# INPUT SAMPLE:
#
# Your program should accept a file as its first argument. The file contains input strings, one per line.
# 
# For example:
# hat
# abc
# Zu6
# 
# OUTPUT SAMPLE:
# 
# Print to stdout the permutations of the string separated by comma, in alphabetical order.
# 
# For example:
# 
# aht,ath,hat,hta,tah,tha
# abc,acb,bac,bca,cab,cba
# 6Zu,6uZ,Z6u,Zu6,u6Z,uZ6

import sys
from itertools import permutations

with open(sys.argv[1]) as f:
    for line in f:
        x = [''.join(x)  for x in permutations(line.rstrip('\n'))]
        x.sort()
        print(",".join(x))
f.close()
