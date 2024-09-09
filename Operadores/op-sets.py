#Operations with sets/conjuntos

set_countries_1 = {'col','mex','bol'}
set_countries_2 = {'pe','bol'}

set_countries_3 = set_countries_1.union(set_countries_2) #.union shows the elements in two sets
#Result is the same, but the syntax is different
#print(set_countries_3) #col, mex, bol, pe
#print(set_countries_1 | set_countries_2)

set_countries_3 = set_countries_1.intersection(set_countries_2)#.intersection shows the elements that are repeated in two sets
#print(set_countries_3) #bol
#print(set_countries_1 & set_countries_2)

set_countries_3 = set_countries_1.difference(set_countries_2)#.difference remove the elements in A that you have in set B
#print(set_countries_3) #col and mex
#print(set_countries_1 - set_countries_2)

set_countries_3 = set_countries_1.symmetric_difference(set_countries_2)#.symmetric_difference a join is made and leaves out duplicate elements
#print(set_countries_3) #col, mex, pe
#print(set_countries_1 ^ set_countries_2)

"""
.union -> shows the elements in two sets / You can also use |

.intersection -> shows the elements that are repeated in two sets / You can also use &

.difference -> remove the elements in A that you have in set B / You can also use - 

.symmetric_difference -> a join is made and leaves out duplicate elements / You can also use ^
"""

#EXCERCISES 
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm,centralAm,southAm) #Solution 1
new_set2 = countries | northAm | centralAm | southAm #Solution 2
#print(new_set)
print(new_set2)