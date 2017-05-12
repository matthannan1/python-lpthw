class Parent(object):
    def implicit(self):
        print "PARENT implicit"

class Child(Parent):
    # Nothing new in this class...yet
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
