#create and print a dictionary

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)

#duplicates not allowed

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dict)

#Length of Dictionary

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(dict))

#Datatype of Dictionary

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dict))

#Accessing Items 

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict["model"])

#Accessing Items 
#acces with the help of get()

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict.get("model"))

#Get keys

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict.keys())

#get values

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict.values())

#get items

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict.items())

#change values 

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2020
print(dict)

#update dictionary

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.update({"year":2020})
print(dict)

#add items

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["color"] = "red"
print(dict)

#looping through a dictionary

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dict:
    print(x)

#nested dictionary 

myfamily = {
  "child1" : {
    "name" : "anu",
    "year" : 2004
  },
  "child2" : {
    "name" : "isha",
    "year" : 2007
  },
  "child3" : {
    "name" : "jashan",
    "year" : 2011
  }
}

print(myfamily)