#!/usr/bin/python
"""
Script simulate cat command
"""
import argparse
import logging


def cat(filename):
    """
    Print file's content.
    """
    logging.basicConfig(filename=filename, level=logging.DEBUG)
    logging.debug('Open this file')
    logging.info('hello')
    logging.warning('1234')
    try:
        with open(filename) as f:
            for line in f:
                print line.rstrip()
    except IOError:
        print 'File not found!'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Print file's content.")
    parser.add_argument('path', help='Path of file.')
    args = parser.parse_args()
    filepath = args.path
    cat(filepath)
