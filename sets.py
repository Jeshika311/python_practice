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

#Add any item in set

set = {"apple" , "banana" , "cheery"}
set.add("orange")
print(set)

#update set

set1 = {"apple" , "banana" , "cheery"}
set2 = {"pineapple" , "mango" , "papaya"}
set1.update(set2)
print(set1)

#Add any iterable

set = {"apple" , "banana" , "cheery"}
list = ["pineapple" , "mango" , "papaya"]
set.update(list)
print(set)

#Remove set items

set = {"apple" , "banana" , "cheery"}
set.remove("banana")
print(set)

#Discard set items

set = {"apple" , "banana" , "cheery"}
set.discard("banana")
print(set)

#union sets

set1 = {"a" ,"b" , "c"}
set2 ={1, 2, 3}
set3 = set1.union(set2)
print(set3)

#join sets with the help of | operator

set1 = {"a" ,"b" , "c"}
set2 ={1, 2, 3}
set3 = set1 | set2
print(set3)

#join multiple sets 

set1 = {"a" ,"b" , "c"}
set2 = {1, 2, 3}
set3 = {"apple" , "banana" , "cheery"}
set4 = set1.union(set2,set3)
print(set4)