#create a set 

set = {"apple" , "banana" , "cheery"}
print(set)

#True and 1 are considered the same value in sets
#False and 2 are considered the same value in sets

set = {"apple" , "banana" , "cheery" , True , False , 1 , 0 ,2}
print(set)

#length of a set

set = {"apple" , "banana" , "cheery"}
print(len(set))

#type of a set

set = {"apple" , "banana" , "cheery"}
print(type(set))

#loop through the set

set = {"apple" , "banana" , "cheery"}
for x in set:
    print(x)

#check if any element is present in set

set = {"apple" , "banana" , "cheery"}
print("apple" in set)

#check if any element is not present in set

set = {"apple" , "banana" , "cheery"}
print("apple" not in set)
