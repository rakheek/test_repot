#!/usr/bin/python 

import os
import re
import json
import sys
from pprint import pprint


'''---
    A script to parse log file and write json data
        ---'''                 
def fib(n):
    a = 0
    b = 1
    for i in range(0,n):
        temp = a
        a = b
        b = temp + b
    return a
if '__main__':
    for i in range(0, 15):
        print fib(i)
