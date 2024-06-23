#Union of set()Unique values displays
set1={3,5,7}
set2={5,7,9}
set3=set1.union(set2)
print(set3)

# Intersection of set(Common Number)
set4={5,7}
set5={9,5,4,6}
set6=set4.intersection(set5)
print(set6)

# difference of set(Difference between two set)
set7={5,7,9,56.7}
set8={1,3,5,10}
set9=set7.difference(set8)
print(set9)

# Print subset or not(means set 11 element present in set10 or not)
set10={1,3,4,5,6,7}
set11={3,4,5,6}
set12=set11.issubset(set10)
print(set12)