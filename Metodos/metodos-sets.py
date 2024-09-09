"""
We can operate sets with other sets, union between sets, intersection between sets and know the difference between several sets.
"""

#Repeated items are not showed on the screen
set_countries = {'mex','co','pe','us','mex',}
print(len(set_countries))
#print(set_countries) #print 4

print('arg' in set_countries) #print False
print('mex' not in set_countries) # False

set_countries.add('ca') #Add an element to the end of the set
#print(set_countries) 
set_countries.update({'bo','ec'}) #update the first set with another set
#print(set_countries) 
set_countries.remove('co') #Remove an element, if it does not exist it returns an error
#print(set_countries) 
set_countries.discard('mexico') #Remove an element, if it does not exist, it does nothing
#print(set_countries) 
set_countries.clear() #Borra ToDO ALV
print(len(set_countries))


"""
.add -> Add an element to the end of the set

.update -> Update the first set with another set

.remove -> Remove an element, if it does not exist it returns an error

.discard -> Remove an element, if it does not exist, it does nothing

.clear -> Delete all

"""