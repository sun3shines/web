

def get():
    
    a = '111'
    yield a
    print 'print a',a
    print 'finished a'
#    yield a

def b():

    f = get()
    e = next(f)
    try:
        next(f)
    except StopIteration:
        pass

    print 'print e',e
    print 'finished b'

b()
