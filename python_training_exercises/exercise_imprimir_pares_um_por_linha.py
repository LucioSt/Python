#!/usr/bin/env python
#
# Sample code to read in test cases:
# INPUT SAMPLE:
#
# Print the even numbers, from 1 to 99, one per line
#


y = [x for x in range(100) if (x%2!=0)]
print(*y, sep='\n')
