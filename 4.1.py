import time
x = time.time()
count = 0
# a + 13*b/c + d + 12*e - f - 11 + g*h/i - 10 == 66
# a + d - f + 12*e == 87 - (13*b/c + g*h/i)

# Min(a + d - f + 12*e) == 1 + 1 - 9 + 12*1 == 5          
# ==> Max(13*b/c + g*h/i) == 87 - 5 == 82

# Min(13*b/c + g*h/i) ==  13*1/9 + 1*1/9 == 14/9.0          
# ==> Max(a + d - f + 12*e) == 87 - 14/9.0


for b in xrange(1,10):
    for c in xrange(1,10):
        for g in xrange(1,10):
            for h in xrange(1,10):
                for i in xrange(1,10):
                    if (14/9.0) <= (13.0*b/c + float(g)*h/i) <= 82:
                        for d in xrange(1,10):
                            for f in xrange(1,10):
                                for e in xrange(1,10):
                                    a = 87 - (13.0*b/c + d + 12*e - f + float(g)*h/i)
                                    if a in xrange(1,10):
                                        count += 1


print count
print time.time() - x




# 447513