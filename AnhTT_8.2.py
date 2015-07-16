#!/usr/bin/python

import sys


def list_methods(module_name):
    funcs = []
    classes = []
    try:
        with open(module_name) as f:
            for line in f:
                if line.rstrip().startswith('def'):
                    funcs.append(line.split('(')[0].split()[1])
                if line.rstrip().startswith('class'):
                    classes.append(line.split()[1].rstrip(':'))
            return funcs, classes
    except IOError:
        print 'No such mudule:', module_name
        sys.exit()

if __name__ == '__main__':
    try:
        methods = list_methods(sys.argv[1])
        print 'There are %i functions:\n' % len(methods[0])
        for func in methods[0]:
            print func
        print '\nThere are %i classes:\n' % len(methods[1])
        for cls in methods[1]:
            print cls
    except IndexError:
        print 'Plese enter a modulename!'
