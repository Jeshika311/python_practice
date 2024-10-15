fruits = ["apple", "banana", "orange"]
color = ["red" , "yellow" , "orange"]

#print all elements 
for x in fruits:
   print(x)

   #break statement
   if x == "banana":
      break         

   #continuous statement
   if x == "apple":
      continue

   
#nested loop
for x in fruits:
  for y in color:
     print(x,y)

 