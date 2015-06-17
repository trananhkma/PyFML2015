def last_bin_digits(n):     # 3.1
    '''
    Return last bin digits of n from 1
    '''
    bin_num = bin(n)
    return bin_num[bin_num.rfind('1'):]

def check_num(n):           # 3.2
    '''
    Return "this is negative number" if n < 0
    Return "this is zero" if n = 0
    Return "this is positive number" if n > 0
    '''
    if n < 0:
        return "This is negative number"
    elif n == 0:
        return "This is zero"
    else:
        return "This is positive number"

def remove_ext(s):          # 3.3
    '''
    Remove the extension of a filename s
    '''
    return s[:s.rfind('.')]
    
def amazing_func(r):        # 3.4
    '''
    No description
    '''
    for i,j in enumerate(r[2:]):
        print i+1, j

def check_month(m):         # 3.5
    '''
    Return number of day in a month
    '''
    months_days = ['January 31', 'February 28', 'March 31', 'April 30',
            'May 31', 'June 30', 'July 31', 'August 31', 'September 30', 
            'October 31', 'November 30', 'December 31'
    ]
    return months_days[m-1]
    
def unique_chars(s):         # 3.6
    '''
    Return unique chars list of a string
    '''
    return [chr for chr in s.replace(' ', '') if s.count(chr) == 1]

def divisible_of_5(r):        # 3.7
    '''
    Return list of divisible numbers of 5 
    '''
    return [num for num in r if num % 5 == 0]
    
def divisible_of_3_and_5(r):    # 3.8
    '''
    Return sum of divisible numbers of 3 and 5
    '''
    return sum([num for num in r if num % 3 == 0 and num % 5 == 0])

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
    count = 1
    num = 3
    while count < 10:
        if is_prime(num) == True:
            primes.append(num)
            count += 1
            num += 2
            continue
        else:
            num += 2
    return primes


print last_bin_digits(99193939948)                  # 100
print check_num(10)                                 # This is positive number
print remove_ext('lauxanh.us.com.vn.jpg')           # lauxanh.us.com.vn
print amazing_func(range(16))                       # right result   
print check_month(5)                                # May 31
print unique_chars('cho meo chim chuot')            # ['e', 'i', 'u', 't']
print divisible_of_5(xrange(100))                   # [5, 10, 15, ... , 95]
print divisible_of_3_and_5(xrange(1000))            # 33165
print func_of_god()                                 # very nhieu ket qua
print first_10_primes()                             # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    
    