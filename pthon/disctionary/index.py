# dictionary is just like an object in js
#there is key value pair 

students={
    "name":"Tufail abbas",
    "age":23,
    "profession":"web developer"
}

print(type(students))

# we can initialize dictionary is empty
#it is very fast way to get data from the store
#it is mutable
#get value through indexed means buy direct key
favBook={}

favBook.update({"book1":"Math","book2":"English"})
print(favBook.keys()) #it will return only the key 
print(favBook.values()) #it will return only the values

print(favBook["book1"]) # in BigO 1 it will return the value Math
print(favBook.get("book1")) # if not pr
print(favBook["book10"]) # it will return error
print(favBook.get("book10")) # if not preset it will return none
urdu_to_english = {
    "madad": "help",
    "kitab": "book",
    "dost": "friend",
    "pani": "water",
    "khana": "food"
}


userValue=input("enter word to translate in english : ").lower()
print(urdu_to_english[userValue])


 