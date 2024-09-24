# import sys;

# print("Hello Python")
# print("Adarsh Tiwari")
# print(sys.version)
# print("sita-ram")

# name = input("Enter your name : ")
# print("Hello " + name)


# if 5 > 2 :
#     print("Five is greater than two")
    
    
# if 5 > 2 : 
#     print("Five is greater  # syntax error
#            than two")


#  The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# if 5 > 2 : 
#     print("Five is greater than two")
#     if 5 > 2 : 
#         print("Five is greater than two")


# if 5 > 2 : 
#     print("Five is greater than two")
#     print("Five is greater than two")
    
    
    
# you have to use same number of space in the same block of code , otherwise Python will give you an error.
# if 5 > 2 : 
#     print("Five is greater than two")   # \\ error
#         print("Five is greater than two")


# Python doex not really have a syntax for multiline comments.
# to add a multiline comment you could insert # for each line.


"""
you can use a multiline string.

Since python will ignore string literals that are not assigned to a variable,
you can add a multiline string (triple quotes) in your code, and place your comment insid it:

> as long as the string is not assigned to a variable , pytom will read the code, but then ignore it,
and you have made a multiline comment.
"""

"""
This is a comment
written in 
more  than just one line
"""


# Variables : variables are containers for storing data values.

# Creating Variable : python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.


# x = 5 
# y = "ram"
# print(x)
# print(y)


# variables do not need to be declared with any particular type, and can even change type after they have been set.
# x = 4 # x is of type int 
# x = "adarsh" # x is now of str
# print(x)


# Casting : if you want to specify the data type of a variable, this can be done with casting.

# x = str(3) # x will be '3'
# y = int(3)  # y will be 3 
# z = float(3) # z will be 3.0
# print(x)
# print(y)
# print(z)


# Get the type : you can get the data type of a variable with the type() function.
# x = 5
# y = "adarsh"
# print(type(x))
# print(type(y))


# Single or Double Quotes : String variables can be declared either by using single or double quotes.
# x = "adarsh"
# x = 'adarsh' # x is the same as
# print(x)


# Case-Sensitive : variable name are case-sensitive.
# a = 4
# A = "ram" # A will not over write a
# print(a)
# print(A)



# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


# Multi Words Variable Names
# Camel Case : myVariableName
# Pascal Case : MyVariableName
# Snake Case : my_variable_name


# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

# a, b, c = "adarsh", "kumar", "tiwari"
# print(a)
# print(b)
# print(c)


# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

# a=b=c = "ram"
# print(a)
# print(b)
# print(c)

# fruit = ["apple", "banana", "grapes"]
# a, b, c = fruit
# print(a)
# print(b)
# print(c)


# x = "adarsh"
# y = "kumar"
# z = "tiwari"
# print(x,y, z)  # In the print() function, you output multiple variables, separated by a comma:

# x = "adarsh"
# y = "kumar"
# z = "tiwari"
# print(x + y + z)  # You can also use the + operator to output multiple variables:


# x = 10
# y = 5
# print(x+y)

# a = 10
# b = "adarsh"
# print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# a = 10
# b = "adarsh"
# print(a,b)


# Global variable : variable that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of function and outside.

# x = "ram"  # Global variable
# def myfunc()    # This will print the value of x, which is "ram"
#     print(x)
#     myfuncfun()  # This is a recursive call to the function itself


# x = "adarsh"   # Global fun
# def fun():
#     x = "ram" # local fun
#     print(x)
    
#     fun()
#     print(x)


# The global Keyword : To create a global variable inside a function, you can use the global keyword.: If you use the global keyword, the variable belongs to the global scope:

# def myfunc():
#     global x
#     x = "ram"
#     myfuncfun()
#     print(x)


# x = "adarsh"
# def myfunc():
#   global x
#   x = "ram"
# myfunc()
# print(x)




# Python Data Types : Built-in Data Types , 

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Getting the Data Type :  You can get the data type of any object by using the type() function: 

# x = 5
# print(type(x))


# a = "Hello"
# b = 1 
# c = 1.5
# d = 1j
# e = ["apple","banana"]
# f = ("apple", "banana")
# g = range(6)
# h = {"name":"adarsh","age":20}
# i = {"apple", "banana"}
# j = frozenset({"apple", "banana"})
# k = True
# l = b"Hello"
# m = bytearray(5)
# n = memoryview(bytes(5))
# o = None

# print(a)
# print(type(a))

# print(b)
# print(type(b))

# print(c)
# print(type(c))

# print(d)
# print(type(d))

# print(e)
# print(type(e))

# print(f)
# print(type(f))

# print(g)
# print(type(g))

# print(h)
# print(type(h))

# print(i)
# print(type(i))

# print(a)
# print(type(j))

# print(a)
# print(type(j))

# print(k)
# print(type(k))

# print(l)
# print(type(l))

# print(m)
# print(type(m))

# print(a)
# print(type(n))

# print(a)
# print(type(n))

# print(o)
# print(type(o))



# int :  Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# a = 35656222554887711
# b = -3255522
# print(type(a))
# print(type(b))


# float : Float can also be scientific numbers with an "e" to indicate the power of 10.
# a = 5e3
# print(a)


# Type Conversion  : You can convert from one type to another with the int(), float(), and complex() methods:

# x = 5
# a = float(x)
# print(a)

# Random Number : Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers: , 
# import random
# print(random.randrange(1, 10))


# x = "3"
# print(type(x))

#print("i am 'adarsh'")

# a = "Hello"
# print(a)

# a = "Hello i am"
# print(a)

# a = """ Hello Mr. adarsh
# Kumar Tiwari """
# print(a)

# a = '''Hello Mr. Python'''
# print(a)

# a = "ram"
# print(a[0])

# for a in "ram":
#     print(a)


# a = "adarsh"
# print(len(a))

# a = "Good morning adarsh"
# print("morning" in a)

# a = "hey adarsh what's up"
# if "adarsh" in a:
#     print("yes", "adarsh is present")

# a = "hey adarsh what's up"
# print("ada" not in a)


# a = "adarsh, tiwari"
# print(a[1:4])  # Slicing Strings
# print(a[1:])
# print(a[:6])
# print(a[-2:-1]) # Negative Indexing : Use negative indexes to start the slice from the end of the string:
# print(a[-3:-2])

# a = " ram sita"
# print(a.upper())
# print(a.lower())
# print(a.strip()) # Remove Whitespace
# print(a.replace("r","s"))
# print(a.split())

# a = "hello"
# b = "Python"
# print(a+b)
# print(a + " " + b)

# age = 10
# name = "adarsh"
# print(age + name) # can not add str + int


# age = 10
# name = f"adarsh {age}" # F-Strings : f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
# print(name)

# price = 20
# text = f"the price is {price} ruppes"
# print(text)

# price = 20
# text = f"the price is {price:.2f} ruppes" # return flolat value
# text1 = f"the price is {price:2f} ruppes" 
# print(text)
# print(text1)

# price = 20
# text = f"the price is {10*5+price} ruppes"
# print(text)

# a = "hello i am \"adarsh\" tiwari"
# print(a)

# *  All string methods return new values. They do not change the original string.


# a = "adarsh tiwari"
# b = " 10 adarsh tiwari"
# c = "Adarsh Tiwari"
# d = "ram"
# e = "ram is my best ram friend ram"
# print(a.capitalize()) # Convert the first character to upper case
# print(b.capitalize())
# print(c.casefold()) # This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
# print(d.center(20)) #  taking up the space of 20 characters
# print(d.center(20, "1"))
# print(e.count("ram")) #  Required. A String. The string to value to search for
# print(e.count("ram", 0, 5)) # string.count(value, start, end)
# print(a.encode()) # Returns an encoded version of the string
# print(e.endswith("friend ram")) # The endswith() method returns True if the string ends with the specified value, otherwise False.
# print(a.endswith("adarsh", 5,20)) # string.endswith(value, start, end)



# Boolean : Booleans represent one of two values: True or False.
# print(10>9)

# print(bool("Hello"))
# print(bool(10))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool()) # In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.



# python operator .

# print(2**3)
# print(10//2)
# print(15//7)

# Operator Precedence

# print((6+3)-(6+3))
# print(100+5*3) # * has higher precedence than + 
# print(100-3**3)
# print(100+~3) # bitwise not has higher pre. than add
# print(8>>4-2) # Bitwise right shift has a lower pre. than sub. and we need to calculate the subs. first
# print(6&2+1) # and has a lower pre. than add. and we need to cal. the addi. first
# print(1 or 2 and 3) # and operator has a higher pre. than or, and we need to cal. the and expression first
# print(5+4-7+3) # add and sub have the same pre. , and we need to cal form left to rigth

# a = 10
# b = 1.2
# c = 5
# d = int("5")
# print(a+b)
# print(a/c)
# print(a+d)

# a = int (input())
# print(a)

# str = "adarsh"
# print(str[0])
# a = str[0]="b"
# print(a) # not allowed


# student = ["adarsh","student","write"]
# student[0] = "pawan"
# print(student[0])
# a = len(student)
# print(a)


# list = [10,20,30,40]
# list.append(50)
# print(list)

# val = input("Enter some value : ")  # all input type str
# print(type(val), val)

# val = int(input("Enter value"))  using type casting
# print(type(val), val)

# first = input("enter 1st num") # input type str
# second = input("Enter 2nd num")  # input type str
# print(first+second)

# first = int(input("enter 1st num"))  # this is type casting str to int 
# second = int(input("Enter 2nd num")) 
# print(first+second)


# list = [2,3,5]
# print(list.sort())  # assending order
# print(list)
# print(list.sort(reverse=True)) # dissanding order
# print(list)

# list in mutable but tuple is immutable and string is immutable
# Tuple

# tup = (10,20,30)
# print(type(tup))
# print(tup[0])

# tup = (1)
# print(type(tup)) # this is int
# print(tup)

# tup = (1,) # this is tuple
# print(type(tup))  
# print(tup)


# Dictionary in Pyton : Dictionary are used to store data values in key:value pairs
# THey are unordered, mutable(changeable) & don't allow duplicate keys

# info = {
#     "key" : "value",
#     "name" : "adarsh",
#     "age": 35,
#     "is_adult" : True,
#     "subject" : ["java", "cpp"],
#     "topic" : ("set", "char")
# }
# print(type(info))
# print(info)
# print(info["name"]) # one value print karne ke liye

# info["name"] = "adarsh kumar tiwari" # add value  , number ve de sakte hai
# print(info)


# dict = {}
# dict["name"] = 'adarsh' # null dict to add value
# print(dict)


# student = {
#     "name" : "adarsh",
#     "subject" : {
#         "phy" : 97,
#         "che" : 92,
#     }
# }
# print(student["subject"]["phy"]) # nested dis
# print(student.keys()) # only return outer keys
# print(list(student.keys()))
# print(len(student.keys()))
# print(student.values())
# print(student.items())
# print(student["name"])
# print(student.get("name"))

# student.update({"city" : "Rewa", "age" : 22})
# print(student)


# Set : set is the collection of the unordered items. , each element in the set must be unique & immutable
# set mutable , but set element immutable

# collection = {1,2,3,4,5 , "hello","world","world"} # ignore dublicate value
# print(collection)
# print(type(collection))

# collection = set ()
# collection.add(1)
# collection.add(2)
# print(collection)
# collection.remove(1)
# print(collection)


# collection = {"Hello","apple","world","java"}
# print(collection.pop()) # random value print karte hai, collection data se


# set1 = {1,2,3}
# set2 = {1,3,4,5}
# print(set1.union(set2)) # no dublicate value
# print(set1.intersection(set2)) # dono me common value


# value = {9, 9.0, 8,8.25, "9.0"}
# print(value)



value = {
    ("float",9.0),
    ("int",9)
}
print(value)