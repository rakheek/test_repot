#!/usr/bin/python 

import os
import re
from pprint import pprint


'''---
        a script to find unique phone numbers in a text file
        accepts following phone patterns
        408-786-7213
        (408)787-7213
        408.987.7213
        408 987 7213
        1-408-922-1234
        ---'''                 

def find_uniq_phn():
    phone_list = []
    phone_list1 = []
    #phonepattern = ["r'(\d{3})-(\d{3})-(\d{4})'", "r'(\(\d{3}\))(\d{3})-(\d{4})'"]
    phonepattern = re.compile(r'(\d{3})\D+(\d{3})\D+(\d{4})')
    fp = open("large.txt", "r")
    lines = fp.read().splitlines()
    for line in lines:
        print line
        phone_numbers = re.findall(phonepattern, line)
        for phone_number in phone_numbers:
            phone_list.append(phone_number)
    for numbers in set(phone_list):
        phone_list1.append( "-".join(numbers))
    pprint(phone_list1)

def main():
    find_uniq_phn()
        
if '__main__':main()
