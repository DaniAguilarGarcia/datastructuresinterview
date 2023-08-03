#receiving input

name = input("what is your name? ")
print("Hello " + name) #concantination

#loops

numbers = [1,2,3,4,5]
for item in numbers:
    print(item) #prints all items in the list

# while loop

i = 0 
while i < len(numbers):
    print(numbers[i])
    i = i + 1 #increment, also prints all items in the list

#range function

range(5) #range object can store a sequence of numbers

numbers = range(0,5) # 0 to 5 excluding 5

for number in numbers:
    print(number)

#tuples are immutable

numbers = (1,2,3) #() for tuples
#no methods like append only count and index

#arguments: information passed into a function
 # **kwards: arbitrary keyword arguments, if you dont know how many arguments will be passed
 # default parameter value
 #pass statement: when we have an empty function to avoid errors

 #Recursion: defined function can call itself, you can loop through data to reach a result
#Lambda can tke any number of arguments, but can only have one expression

#the __init__() function, executed when the class is being initiated , use it to assign values to object properties
#object methods: methods in objects are functions that belong to the object
#self parameter is reference to the current instance of the class, and used to access variables that belong to the class
# self can be any word, but it has to be at the beggining (first parameter)
#modify object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(abc):
        print("Helo my name is " + abc.name)

p1 = Person("John", 36)

p1.age = 40 # change p1 age
del p1.age # delete p1 age property

#inherutance, a class that inherits all the methods and properties from another class
#parent class is the class being inherited form, so the base class
#child class is the class that inherits from another class, or derived class


#the childs __init__() function overrides the inheritance of the parents __init__() function
#o keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
#use the super() function , will make the child class inherit all the methods and properties from its parents
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

#iterators 
#looping through an iterator: 
mytuple = ("apple", "banana" , "cherry")

for x in mytuple:
    print(x)
#create an iterator:
# __iter__() must always return the iterator object itself

# __next__() must return the next item in the sequence

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

#stop iteration StopIteration

#scope:  a variable is only available from inside a region it is created.

import modulefinder
from importlib import x
import datetime
 #create date objects
 #strtime()
 #from json to python

import json
from typing import OrderedDict 
  
x=  '{"name":"John", "age":30}'

#parse x:

y = json.loads(x)
#results its a python dictionary 
print(y["age"])

#from python to json

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#sort result

json.dumps(x, indent=4, sort_keys=True)

#RegEx: regular expressions : sequence of characters that forms a search pattern.
# can be used to check if a string contains the specified search pattern

import re

#check the string to see if it tarts with "the" and ends with "spain"

import re 

txt = "The rain in spain"
x= re.search("^The.*Spain$", txt)

#findall

import re 

txt = "The rain in Spain"
x = re.findall("ai", txt)

print(x)

#sub() replaces the matches with the text of your choice


#insertion:

mylist.insert(index, item)

#pop will return the last item and removes it

#remove specific element

mylist.remove("item")
mylist.clear #removes 
mylist.reverse()
mylist.sort #ascending Order
new_list = sorted(mylist)

#slicing for accessing parts of your list

a = mylist[1:9]

#reverse list:

a = mylist[::-1]

.copy() to make a copy

b = [i*i for i in mylist]

#tuples, ordered and inmutable, allows duplicate

mytuple = ("max", 28, "Boaston")

#object oriented programming https://www.youtube.com/watch?v=ZDa-Z5JzLYM
#methods: function associated with a class
#class: blue print for creating instances
#instance variables: contain data that is unique
#class variables:

class Employee:
    def __init__(self, first, last, pay): #initialized or  constructor self and other arguments
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    emp_1 = Employee('Corey', 'Schefer', 50000)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    print(emp_1.fullname())
        
# if __name__ == __main__:

def main():
    pass
if __name__ == '__main__':
    main()


#focus on =  
#Big(O), learn cheat sheet
#Sorting, no bubble sort, know at least one n*log(n) learn quick sort and merge sort)
#hashtables, using arrays
#trees: constroction, traversal and manipulation algo. 
# one balanced binary tree red/black tree, a splay tree or an AVL tree, and know how it's implemented.
#BFS and DFS, know the difference inorder, postorder and preorder.
#Graphs: (objects and pointers, matrix, and adjacency list, breadth-first search and depth-first search.
#Dijkstra and A*.
#NP-complete problems, such as traveling salesman and the knapsack problem
#combinatorics and probability. You should be familiar with n-choose-k problems and their ilk

