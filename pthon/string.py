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
print("n--",n)
#we can do from negative index also 
print("cp- ",cp[-4:-1])
print("cp+ ",cp[1:4])