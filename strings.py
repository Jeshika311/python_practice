#we can write strings in single , double or triple quotes

a = "It's alright"  #Assigning string to a Variable
print(a)

print("He is called 'Juhi'") #Display string literal with the print() function

#length of the string

txt = "My name is John"
print(len(txt))

#slicing strings

b = "Hello, World!"  #slicing by positive indexing
print(b[2:5])

c = "Hello, World!"  #Slice From the Start
print(c[:5])

d = "Hello, World!"  #Slice To the End
print(d[2:])

f = "Hello, World!"  #Negative indexing
print(f[-5:-2])

#modify strings

a = "Hello, World!"  #upper case
print(a.upper()) 

a = "Hello, World!"  #lower case
print(a.lower())

a = " Hello, World! "  #remove whitespace
print(a.strip())
 
a = "Hello, World!"  #replace string
print(a.replace("H", "J"))

a = "Hello, World!" #split string
print(a.split(",")) 

#string concatenation

a = "Hello"  
b = "World"
c = a + " " + b
print(c)

#string format

age = 36
txt = f"My name is John, I am {age}"
print(txt)