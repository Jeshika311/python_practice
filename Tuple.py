L = (10,20,30,35,40,45,50)
L1 = (15,25,75)

#To find total number of elements in a tuple

print(len(L))

y = list(L)
x = list(L1)

#Insert new element in tuple
y.insert(4,75)
L = tuple(y)
print(L)

#append tuple
y.append(95)
L = tuple(y)
print(L)

#extend tuple
y.extend(x)
L = tuple(y)
L1 = tuple(x)
print(L)

#remove an element from tuple
y.remove(35)
L = tuple(y)
print(L)

#remove with the help of pop operation
y.pop(4)
L = tuple(y)
print(L)
