# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#args is actually pointless, so we can do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothing."


print_two("Matt", "Hannan")
print_two_again("Matt", "Hannan")
print_one("First!")
print_none()
    
