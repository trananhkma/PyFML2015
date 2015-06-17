# -*- coding: utf-8 -*-

# Import python libs
import random


def rand_str():
    '''
    Return a random 32 chars string
    '''
    chars = string.ascii_lowercase + string.digits
    rand_str = ''.join(random.choice(chars) for x in range(32))
    return rand_str
    
def contains_whitespace(text):
    '''
    Returns True if there are any whitespace characters in the string
    '''
    return ' ' in text



