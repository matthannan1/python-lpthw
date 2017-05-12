class Parent(object):

    def implicit(self):
        print "PARENT implicit"

class Child(Parent):
    def override(self):
        print "CHILD override"

    def implicit(self):
        print "CHILD implicit"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
