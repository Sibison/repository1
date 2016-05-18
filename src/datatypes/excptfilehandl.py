def div(a,b):
    opt=0
    try:
        print 1
        opt=a/b
        print 2
        #except ZeroDivisionError,z:
        print z
        #except Exception,t:
        print t
    else:
        print 'no exp'
        finally:
        print "finally"
        return opt
print div(2,2)