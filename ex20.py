#import argv
from sys import argv

# take in the file and file name
script, input_file = argv

# define function print_all and take in f, which is "current_file"
def print_all(f):
    #read the contents of the file and print them out
    print f.read()

# define function rewind and take in f, which is "current_file"
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print "\nFirst let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)
