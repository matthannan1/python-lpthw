# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in the m
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'Troy'
cities['OR'] = 'Portland'

# print out some cities
print
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbrviation is: ", states['Florida']

# do it by using the state then cities dict
print
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print
print '-' * 10
for abbrev, city in cities.items():
    print "%s has city %s" % (abbrev, city)

# now do both at the same time
print
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print
print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print "Sorry, Texas does not exist."

# get a city with a default value
print
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
