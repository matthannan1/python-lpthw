# ex37.py is to test out a little of this and a little of that.
# The list is fairly lengthy.

# and, =, if, print, %d
a = 1
b = 1
if a and b:
    print "a is %d and b is %d. They are equal." % (a, b)

# with and as are used together...to run parallel commands.
# can be used for more than opening, writing and closing text files
with open('output.txt', 'w') as f:
    f.write('Hi there!')


# assert is used to EXPLICITLY set a state
# An assertion is a sanity-check that you can turn on or turn off
# when you are done with your testing of the program.
