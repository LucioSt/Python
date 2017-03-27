#!/usr/bin/env python
# Time func user exercise 

import time
from time_func import clock

@clock
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    snooze(.123)

