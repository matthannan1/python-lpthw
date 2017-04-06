# import argv module
#from sys import argv
# set the arguments
#script, filename = argv
# create file object named txt
#txt = open(filename)
# print out the file name
#print "Here's your file %r:" % filename
# read the contents of the txt file object
#print txt.read()
# ask user for file name again...for some reason
#print "Type the file name again:"
# assign input to variable
#file_again = raw_input("> ")
# create file object named txt_again
#txt_again = open(file_again)
# read and print out the contents of the file object txt_again
#print txt_again.read()
# Study Drill part 5
# ask user for file name again...for some reason
print "Type the file name again:"
# assign input to variable
file_again = raw_input("> ")
# create file object named txt_again
txt_again = open(file_again)
# read and print out the contents of the file object txt_again
print txt_again.read()
