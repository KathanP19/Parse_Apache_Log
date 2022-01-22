#!/bin/python3

from fileinput import filename
import re
import sys
import os
from optparse import Option, OptionParser
from tabnanny import verbose

def readfile(f,v):
    openfile = open(f,"r")

    unique_outfile = open("uniqueIP.txt","w")
    all_outfile = open("allIP.txt","w")
    ipAndUrl_outfile = open("ipAndUrl.txt","w")

    lines = []
    ipAndUrl = {}
    ip_list = set()

    for line in openfile:
        lines.append(line.strip('\n'))

    for line in lines:
        ip = line.split(" ")[0]

        if ip in ipAndUrl:
            ipAndUrl[ip].append(line.split(" ")[6])
        else:
            ipAndUrl[ip] = [line.split(" ")[6]]
        
        all_outfile.write(ip)
        all_outfile.write("\n")

        ip_list.add(ip)

    for ip in ip_list:
        unique_outfile.write(ip)
        unique_outfile.write("\n")

    if v == True:
     for ipUrl in ipAndUrl:
         print(ipUrl, "\t", ipAndUrl[ipUrl], "\n")

    for key, value in ipAndUrl.items(): 
        ipAndUrl_outfile.write('%s  %s\n' % (key, value))

    unique_outfile.close()
    ipAndUrl_outfile.close()
    all_outfile.close()
    openfile.close()

def Main():
    #define options
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",help="Path of you apache log file.", metavar="FILE")
    parser.add_option("-v", "--verbose", action="store_true",dest="verbose", default = False,help="Verbose Mode.")
    (options, args) = parser.parse_args()

    print(options.filename)
    if (options.filename == None):
            print (parser.usage)
            exit(0)
    else:
            file = options.filename
          
    # function calling
    result = readfile(file,options.verbose)
# Driver code
if __name__ == '__main__':
      
    # function calling
    Main()
