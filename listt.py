L = [10,20,30,35,40,45,50]
L1 = [15,25,75]

#check total no. in list

print(len(L))

#Indexing of an element
#position of element

print(L[-1])

#range of list

print(L[2:5])

#Check whether the element is in the list or not 

if 35 in L:
    print ("yes")

#Insert new element in last in list

L.insert(4,90)
print(L)

#Add new no. in list 

L.append(95)
print(L)
