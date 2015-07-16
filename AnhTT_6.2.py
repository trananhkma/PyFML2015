def last_bin_digits(n):     # 3.1
    '''
    Return last bin digits of n from 1
    '''
    try:
        bin_num = bin(n)
        return bin_num[bin_num.rfind('1'):]
    except TypeError:
        print 'Input is not a number'

def check_num(n):           # 3.2
    if isinstance(n, (int, long, float, complex)):
        if n < 0:
            return "This is negative number"
        elif n == 0:
            return "This is zero"
        else:
            return "This is positive number"
    else:
        print 'Input is not a number'
        
def remove_ext(filename):            # 3.3
    '''
    Remove the extension of a filename
    '''
    try:
        index = filename.rfind('.')
    except AttributeError:
        print 'Input is not a filename'
    else:
        if index == -1:
            print 'This file has been removed the extensions'
        else:
            return filename[:index]
    
def amazing_func(numbers):        # 3.4
    try:
        for index, item in enumerate(numbers[2:]):
            print index+1, item
    except TypeError:
        print 'Wrong input'

def check_month(month):         # 3.5
    '''
    Return number of day in a month
    '''       
    months_days = ['January 31', 'February 28', 'March 31', 'April 30',
            'May 31', 'June 30', 'July 31', 'August 31', 'September 30', 
            'October 31', 'November 30', 'December 31'
    ]
    try:
        return months_days[month-1]
    except (TypeError, IndexError):
        print 'Input is not a month of year'
    
def unique_chars(string):         # 3.6
    '''
    Return list of unique chars in a string
    '''
    try:
        new_str = string.replace(' ', '')
    except AttributeError:
        print 'Input is not a string'
    else:
        return [char for char in new_str if new_str.count(char) == 1]

def divisible_of_5(numbers):          # 3.7
    '''
    Return list of numbers divisible by 5 
    '''
    try:
        return [num for num in numbers if num % 5 == 0]
    except (NameError, TypeError):
        print 'Input is not a list of numbers'
    
def divisible_of_3_and_5(numbers):    # 3.8
    '''
    Return sum of numbers divisible by 3 and 5 
    '''
    try:
        return sum([num for num in numbers if num % 3 == 0 and num % 5 == 0])
    except:
        print 'Input is not a list of numbers'

def func_of_god():                     # 3.9
    '''
    0 < a, b, c < 10
    Return list of [a,b,c] if a + b/c = 10
    '''
    return [[a,b,c] for a in xrange(1,10) for b in xrange(1,10) 
            for c in xrange(1,10) if a + float(b)/c == 10
    ]

def is_prime(n):                # 3.10
    '''
    Return True if n is prime number
    '''
    if not isinstance(n, int) or n < 2:
        return False
    else:
        from math import sqrt
        count = 2
        while count <= sqrt(n):
            if n % count == 0:
                return False
            count += 1
        return True

def first_10_primes():
    '''
    Return list of first 10 prime numbers
    '''
    primes = [2]
    num = 1
    while len(primes) < 10:
        num += 2
        if is_prime(num):
            primes.append(num)
            continue
    return primes


def e_bill(count):
    # electricity bill per month
    bill = 0
    costs = {50: 1230, 100: 1530, 'max': 1786}
    if isinstance(count, (int, float, long, complex)):
        if 0 <= count <= 50:
            bill += count*costs[50]
        elif count <= 100:
            bill += 50*costs[50] + (count - 50)*costs[100]
        elif count > 100:
            bill += 50*costs[50] + 50*costs[100] + (count - 100)*costs['max']
    else:
        print 'Input is not a number'
    return bill

def e_bills(counts):
    # electricity bill of multiple months
    try:
        return [e_bill(count) for count in counts]
    except:
        print 'Input is not a list of electricity bills'
        
    
print last_bin_digits(99193939948)                  # 100 
print check_num(-4)                                 # This is positive number
print remove_ext('lauxanh.us.com.vn.jpg')           # lauxanh.us.com.vn
print amazing_func(range(16))                       # right result   
print check_month(5)                                # May 31
print unique_chars('cho meo chim chuot')            # ['e', 'i', 'u', 't']
print divisible_of_5(xrange(100))                   # [5, 10, 15, ... , 95]
print divisible_of_3_and_5(xrange(1000))            # 33165
print func_of_god()                                 # very nhieu ket qua
print first_10_primes()                             # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print is_prime('sdfsdg')
print e_bills([1, 29, 1235, 69, 100])               # [1230, 35670, 2165110, 90570, 138000]  