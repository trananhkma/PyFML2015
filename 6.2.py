def last_bin_digits(n):     # 3.1
    '''
    Return last bin digits of n from 1
    '''
    try:
        bin_num = bin(n)
    except (TypeError, NameError):
        print 'Input is not a number'
    else:
        return bin_num[bin_num.rfind('1'):]

def check_num(n):           # 3.2
    '''
    Return "this is negative number" if n < 0
    Return "this is zero" if n = 0
    Return "this is positive number" if n > 0
    '''
    try:
        n < 0
    except NameError:
        print 'Input is not a number'
    else:
        if isinstance(n, (int, long, float, complex)):
            if n < 0:
                return "This is negative number"
            elif n == 0:
                return "This is zero"
            else:
                return "This is positive number"
        else:
            print 'Input is not a number'
        
def remove_ext(filename):          # 3.3
    '''
    Remove the extension of a filename
    '''
    try:
        x = filename.rfind('.')
    except AttributeError:
        print 'Input is not a filename'
    else:
        if '.' not in filename:
            print 'This file has been removed the extensions'
        else:
            return filename[:x]
    
def amazing_func(r):        # 3.4
    '''
    No description
    '''
    try:
        enumerate(r)
    except TypeError:
        print 'Wrong input'
    else:
        for i,j in enumerate(r[2:]):
            print i+1, j

def check_month(month):         # 3.5
    '''
    Return number of day in a month
    '''       
    months_days = ['January 31', 'February 28', 'March 31', 'April 30',
            'May 31', 'June 30', 'July 31', 'August 31', 'September 30', 
            'October 31', 'November 30', 'December 31'
    ]
    try:
        result = months_days[month-1]
    except (NameError, TypeError, IndexError):
        print 'Input is not a month of year'
    else:
        return result
    
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

def divisible_of_5(range_):          # 3.7
    '''
    Return list of divisible numbers of 5 
    '''
    try:
        result = [num for num in range_ if num % 5 == 0]
    except (NameError, TypeError):
        print 'Input is not a list of numbers'
    else:
        return result
    
def divisible_of_3_and_5(r):    # 3.8
    '''
    Return sum of divisible numbers of 3 and 5
    '''
    try:
        lst = [num for num in r if num % 3 == 0 and num % 5 == 0]
    except:
        print 'Input is not a list of numbers'
    else:
        return sum(lst)

def func_of_god():              # 3.9
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
    if not isinstance(n, (int)) or n < 2:
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
    try:
        count + 1
    except:
        print 'Input is not a number'
    else:
        bill = 0
        costs = {50: 1230, 100: 1530, 'max': 1786}
        if count < 0:
            return bill
        elif 0 <= count <= 50:
            bill += count*costs[50]
            return bill
        elif count <= 100:
            bill += 50*costs[50] + (count - 50)*costs[100]
            return bill
        else:
            bill += 50*costs[50] + 50*costs[100] + (count - 100)*costs['max']
            return bill

def e_bills(counts):
    # electricity bill of multiple months
    try:
        bills = [e_bill(count) for count in counts]
    except:
        print 'Input is not a list of electricity bills'
    else:
        return bills
    

    
    
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