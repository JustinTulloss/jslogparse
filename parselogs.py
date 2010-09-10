#!/usr/bin/env python
import sys

while(True):
    line = raw_input()
    pieces = line.split('---')
    for part in pieces:
        if part.startswith('Log'):
            part = part.replace('Log: ', '')
            print "Tail of the Log:"
            logLines = part.split('::')
            for logLine in logLines:
                print "\t%s" % logLine
        else:
            print part
    print "\n=================================\n"
