#!/usr/bin/env python
# Sample code to read in test cases:
# INPUT SAMPLE:
# 
# The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.
# 
# For example:
# 
# Hello World
# Hello CodeEval
# OUTPUT SAMPLE:
# 
# Print to stdout each sentence with the reversed words in it, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.
# 
# For example:
# 
# World Hello
# CodeEval Hello
# SUBMIT

import sys

with open(sys.argv[1]) as f:
    for line in f:
        x = line.split()
        print(" ".join(x[::-1]))
f.close()
