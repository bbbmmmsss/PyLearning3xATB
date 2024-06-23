#SET
#In set store unique items
# set is unordered
# set is mutable
# set does not support indexing

sets={1,2,3,3,4,5,6,7,8,9,10}
print(sets)

# We can apin pend set
sets.add(11)
print(sets)

# We can del set
sets.remove(11)
print(sets)

# We can count length of stes
print(len(sets))

# Convert set into list
sets=list(sets)
print(sets)
print(type(sets))

