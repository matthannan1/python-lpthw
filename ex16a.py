from sys import argv

script, filename = argv

print "Opening file ", filename
text = open(filename)

print "Here is what it says: "
print "\n"
print text.read()

text.close()
