#list used to store set of values in continuous  memory location
data=[1,"zain","adnan",False,1,3,12,1]
# print(data)
val=data.count(1) # it wil find all 1 and will count how many times it is
print(val)
data.append(0) # it will add at the last
#sort the list 
l1=[1,4,5,3,2,0]
l1.sort()
print(l1)

#we can also add on any index like in 0 or any

l1.insert(0,90) # add on the 0th index
print(l1)

# also we can remove form any index using pop

l1.pop(2)
print(l1)

#remove method

myList=[1,2,3,4,5,1]
# myList.remove(2)  # it will remove first match value from the list

myList.remove(1)   # it will remove only the first 1 present in 0th index
print(myList)
