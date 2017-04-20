def loop(val,incrementor):
    i = 0
    numbers = []
    print val
    for i in range(0,val,incrementor):
        print "At the top, i is %d and val is %d" % (i, val)

        numbers.append(i)
        i = i + incrementor
        print i < val
        print "Nmbers now: ", numbers
        print "At the bottom, i is %d and val is %d" % (i, val)
        print
    print "The numbers: "
    for num in numbers:
        print num

input = raw_input("Enter a low number: ")
val = int(input)
input2 = raw_input("Enter amount to increase the number by: ")
incrementor = int(input2)
loop(val,incrementor)
