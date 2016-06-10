"""Sample code to read in test cases:

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

Hello world!
JavaScript language 1.8
A letter
OUTPUT SAMPLE:

Print results in the following way.

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER
"""
import sys

with open(sys.argv[1]) as file: lines = [line.strip() for line in file]
[print(v.swapcase())  for v in lines]

