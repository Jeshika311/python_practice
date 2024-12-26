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