#create and call a function

def my_function():
  print("Hello from a function")

my_function()

#Pass Arguments from function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Anu", child2 = "Payal", child3 = "Jashan")

#Default Parameter value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)