print [[a,b,c] for a in xrange(1,10) for b in xrange(1,10) 
        for c in xrange(1,10) if a + float(b)/c == 10]