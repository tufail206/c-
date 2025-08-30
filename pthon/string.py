# we can use single ,double and triple in quotes
#triple quotes is used for multi line

address='khaplu saltoro'
poem="""hello 
     this is my poem
     i am writing this for python
     practice 
     """
print(poem)
# string are not mute-able

name="hello coder"


newName=name[3]
print('new name is ',newName)

# name[1]="p"
# print(name)
# error will be
#   name[1]="p"
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment

cp="hello"
# this will print the length of any stirng
#   len(cp)

#slice method  4 will not include
n=cp[0:4]
print("bn--",n)
#we can do from negative index also 
print("cp- ",cp[-4:-1])
print("cp+ ",cp[1:4])

#skip slices
st="acdefgh"
skipSlice=st[1:6:3]
print(skipSlice)
# output will be cf why ? first we will do for [1:6] so from c to f
# (cdef) then
# for  [1:6:3] 3 means  skip every third  from 1(c) so c then 3rd f so cf