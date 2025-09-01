#set is well defined object
# it is same as object but ont the key value pair
# set will have distinct element
# myValue={1,2,3}

# no for empty set we use set function
# name=set() 
# kep in mind    name={} is not empty set ,it's empty dictionary
name=set() 
name.add("tufail")
print(name)

# set1={1,2,3,4,5}
# set2={3,2,1,40,39}

# print(set1.union(set2)) // it will retrun only the value from both but no repeated
#no way to change the set but can add new item 
set1={1,2,3,4,5,1}
set2={3,2,1,40,39}

#print(set1.intersection(set2)) # it will retrun only the same element from both

set1.remove(1) 
print(set1)