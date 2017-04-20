animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
i=0

while i<len(animals)+1:

    if i == 0:
        print "The first (1st) animal is at %d and is a %r." % (i,animals[i])
        print "The animal at %d is the first animal and is a %r" % (i, animals[i])
    i+=1
