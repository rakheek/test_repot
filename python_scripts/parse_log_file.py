#!/usr/bin/python 

import os
import re
import json
import sys
from pprint import pprint


'''---
    A script to parse log file and write json data
        ---'''                 

def parse_into_dict(log_file):
    my_dict = {}
    f_out =open("json_out", "a")
    with open("log_file", "r") as f:
        lines = f.readlines()
    for line in lines:
        splitLine = line.split(" ")
        if(re.match(r"\d+-\d+-\d+", splitLine[0])):
            my_dict.update({'Date':"%s %s" %(splitLine[0], splitLine[1])})
            my_dict.update({'Info':splitLine[5]})
            print my_dict
            json.dump(my_dict, f_out)
        else:
            pass        
    pprint(my_dict)
if '__main__':
    log_file = sys.argv[0]
    parse_into_dict(log_file)
