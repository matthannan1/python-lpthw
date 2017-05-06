## Animal is-a object
class Animal(object):
    pass

## is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ##
        self.name = name

## is-a Animal
class Cat(Animal):
    def __init__(self,name):
        ##
        self.name = name

## is-a object
class Person(object):
    def __init__(self, name):
        ##
        self.name = name
        ##
        self.pet = None

## is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## is-a object
class Fish(object):
    pass

## is-a Fish
class Salmon(Fish):
    pass

## is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## is-a Cat
satan = Cat("Satan")

## is-a Person
mary = Person("Mary")

## is-a Employee
# frank = Employee("Frank, 120000")

## is-a object
#frank.pet = rover
mary.pet = satan

## is-a object
flipper = Fish()

## is-a object
crouse = Salmon()

## is-a object
harry = Halibut()


print "Mary's cat is %s" % mary.pet("satan")
