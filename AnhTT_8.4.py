#!/usr/bin/python

import sys


def tail(filename):
    first_10_lines = []
    try:
        with open(filename) as f:
            for line in f:
                first_10_lines.append(line.rstrip())
                if len(first_10_lines) == 10:
                    break
            return first_10_lines, f.readlines()[-10:]
    except IOError:
        print 'File not found!'
        sys.exit()

if __name__ == '__main__':
   try:
        lines = tail(sys.argv[1])
        print 'First 10 lines in %s:' % sys.argv[1]
        for i in lines[0]:
            print i.rstrip()
        if len(lines[1]) > 0:
            print 'Last 10 lines in %s:' % sys.argv[1]
            for i in lines[1]:
                print i.rstrip()
   except IndexError:
       print 'Plese enter a path of file!'
