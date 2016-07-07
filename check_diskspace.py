#!/usr/bin/python 

import os
import re
from pprint import pprint
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

'''---
        A script to do df and send email if over 80%
        ---'''                 
def send_email(percent_avail):
    
    COMMASPACE = ', '
    Subject = 'Diskspace alert'
    TEXT = 'Diskspace is at %s percent' % percent_avail
    receipients = ['rakheek@yahoo.com', 'rakhee.k@samsung.com']
    FROM = "rakheek@yahoo.com"
    TO = COMMASPACE.join(receipients)
    message = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (FROM, TO, Subject, TEXT)
    
    s = smtplib.SMTP('localhost')
    s.sendmail(FROM, TO, message)
    s.quit()
    
def check_build_disk_space():
    df_output_lines = [s.split() for s in os.popen("df -Ph").read().splitlines()]
    for line in df_output_lines:
        if(line[0] == "/dev/disk0s2"):
            percent_avail = int(line[4].strip(' \t\n\r%'))
            print "This is avaiable %s" % percent_avail
            if( percent_avail > 20):
                print "diskspace is at %s percent - please check" % percent_avail 
                send_email(percent_avail)
#    pprint(df_output_lines)
    
def main():
    check_build_disk_space()
        
if '__main__':main()
