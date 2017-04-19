the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of for-loop goers through a list
for number in the_count:
    print "This is count %d" % number

# Same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can go through mixed lists too
# Notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# We can also build lists, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to list." % i
    # append is a function that lists Understand
    elements.append(i)

# Now we can print them out, too.
for i in elements:
    print "Element was: %d" % i


# directly assign range to list?
elements2 = []
elements2.append(range(10,20))
count = len(elements2)
print "Element2 list contains ", count, " items."
for i in range(0, count):
    print(elements2[i])
# I'll take that as a big old NO!
    
