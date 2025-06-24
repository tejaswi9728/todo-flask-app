##for i in range(1,11):##
   ## print(i)##
##for i in range(1,20):##
   ## if i % 2 == 0:##
       ## print("even numbers:", i)##
##for i in range(1,5):##
    ##square = i * i##
    ##print(i, "squared is:", square)##
##for i in range(1, 10):##
    ##if i == 6:##
        ## break##
   ## print(i)##
##for i in range(1, 10):##
    ##if i == 5:##
       ## continue##
   ## print(i)##
##number = int(input("Enter a number:"))##
##for i in range(1, 10):##
     ##mul = number * i##
     ##print(number, "*", i, "=", mul)##
##name = str(input("Enter your Name:"))##
##for i in name:##
     ##print(i)##
##for i in range(1, 21):##
    ##if i % 2 != 0:##
        ##print("odd numbers:", i)##
##numbers = 0##
##for i in range(1, 11):##
    ## numbers = numbers + i##
     ##print(numbers)###
##for i in range(1, 21): ##oddnumbers##
    ##if i % 2 != 0:##
       ## print("odd numbers:", i)##
##sum = 0
##for i in range(1, 11):
   ## sum = sum + i
   ## print(sum)##
##for i in range(10, 0, -1):##
   ## print(i)##
##n* (n-1)* (n-2) * (n-3) * (n-4) * (n-5) * (n-6) * (n-7) * (n-8) * (n-9) 
##5! = 5*4*3*2*1 = 120##
##num = int(input("Enter a number:"))
##for i in range(1, 30):
   ## mul = num * i
    ##print( "3", "*", i ,"=", mul)##
##word = str(input("Enter a word:"))
##for index in range(len(word)):
   ## print(index , word[index])##

#5! = 5*4*3*2*1 = 120
##factorial
##n = int(input("Enter a number:"))
##t = 1
##for i in range(1, n + 1):
    ##t = t * i
    #print(t)
##fact in while
#n = int(input("Enter a number:"))
#i = 1
#t = 1
#while (i <= n):
   #t = t * i
   #i = i + 1
   #print(t)
#sum of first 5 num in for
#1+ 2+ 3+ 4+ 5 = 15
#t = 0
#for i in range(1, 6):
 #  t = t + i
 #  print(t)
#same in while
#i = 1
#t = 0
#while (i <= 5):
   #t = t + i
   #i = i + 1
  # print(t) 
# table in for
#n = int(input("enter a number:"))
#for i in range(1,6):
    #t = n * i
    #print(t)
#same in while
#i = 1
#n = 2
#while (i <= 5):
   #t = n * i
   #i = i + 1
   #print(t)
#print 1 to 5
#for i in range(1, 6):
    #print(i)
#i = 0
#while (i <= 5):
   #i = i + 1
   #print(i)
#a = int(input("Enter a number:"))
#b = int(input("Enter a second number:"))
#c = a + b
#print(c)
#funtions
#def greet(name):
   # print("Hello", name)

#greet("Reyansh")
#def add(a,b):
   #return a * b

#c = add(5, 6)
#print( "mul is:", c)
##def div_by(a):
    #if  a % 3 == 0:
        #print("it is dividible")

#c = div_by(9)

#def square(n):
    #return n * n

#c = square(2)
#print("suared is :", c)
#name = str(input("Enter your name:"))
#for i in name:
     #print(i)
#def nam(name):
    #for i in name:
        #print(i)
        
        
#nam("Tejaswi")
#def fact(t):
   # for i in range(1, 6):
       # t = t * i
       # print(t)
#fact(1)
#def check_even_or_odd(n):
    #if n % 2 == 0:
       #print("it is even:")
   # else:
      # print("it is odd:")
        
#check_even_or_odd(9)
#SUM OF EVEN NUMBERS BUT WHAT I THINK IS IT IS NOT WORKING
#def sum_of_even(n):
   # Sum = 0
   # for i in range(1, n+1):
       # if i % 2 == 0:
          #  Sum = Sum + i
    #print("Sum of even numbers is:", Sum)

#sum_of_even(10)
#def div_by(a, b):
   # for i in range(a, b + 1):
        #if i % 5 == 0:
           # print(i)
#div_by(1,20)
#def greet(name):
 #   print("Hello", name)
    
#greet("Ravi")
#def mul(a, b):
 #   print("multiplying a and b")
  #  return a * b
#
#result = mul(10, 9)
#print("result is:", result)
#def add(a, b):
 #   return a + b
    
#add(10, 6)
#print(add(10, 6))
#def square(n):
 #   return n * n
#square(6)
#print(square(6))
#def greet(name = "guest"):
 #   print("Hello:", name )

#greet("Tejaswi")
#greet()
#greet("user")
#def mul(a, b = 1):
    
 #   return a + b

#print(mul(3, 5))
#print(mul(5))
#def welcome(name = "user" , city = "hyderabad"):
 #    print("HELLO:", name , "welcome to:", city)

#welcome("Tejaswi")
#welcome()
#def power(base, exponent = 2):
 #   return base ^ exponent
    

#print(power(3))
#print(power(2, 3))

#def greet(name , language = "English"):
 #   if language == "English":
  #      print("Hello:", name)
   # elif language == "Hindi":
    #    print("namaste:", name)
    #elif language == "Tamil":
     #   print("Vanakam:", name)
    #else:
     #   print("Hello:", name)
        
#greet("Tejaswi", "Tamil")
#greet("RAJI")
#def student_info(name, age = 18, course = "Python"):
 #    print("Name:", name)
  #   print("AGE:", age)
   #  print("COURSE:", course)
#student_info("ravi")
#student_info("Anu", 20 , "Java")
#def add_to_cart(item, quantity = 1):
 #   print(item, "added to cart:", "Quantity :", quantity)

#add_to_cart("Laptop")
#add_to_cart("Mouse", 2)
#def welcome(name, city):
 #   print("welcome:", name ,"from the city:", city)

#welcome(name = "Tejaswi", city = "Hyderabad")#keyword arguments
#welcome("Tejaswi", "Hyderabad") #positional arguments
#def student(name, grade, school):
 #   print("student:", name)
  #  print("Grade:", grade)
   # print("School:", school)
#student("tejaswi", grade = "A", school = "vvkn")#mixed positional and keyword arguments
#def book_flight(name, from_city, to_city):
 #   print(name ,"booked a flight from city:", from_city , "To",to_city )
#book_flight(to_city = "hyderabad", from_city = "banglore", name = "Tejaswi")
#def area_of_rectangle(length, width):
     
 #    return length * width 
    
#area = area_of_rectangle(length = 6, width = 7)
#print("Area of rectangle is:" ,area)
#def calculate_area(length, width, unit = "cm2"):
 #    return length * width

#area = calculate_area(5, 4)
#print( "The area is:", {area} , {unit})
#def ticket_movie(name, movie, status):
 #   return f"Hello {name}, your ticket for movie {movie} at 6pm is {status}:!"

#print(ticket_movie("tejaswi", "jailer" , "confirmed"))
#def discount_calculator(item, price , discount_percent):
 #    discount_amount = price * discount_percent / 100
  #   final_amount = price - discount_amount
   #  return f"{item} after discount {discount_percent}% is {final_amount}"
#msg = discount_calculator("Laptop", price = 55000, discount_percent = 10)
#print(msg)
#print(msg)
#def greet(name, age , city = "Delhi"):
   # print("hello my name is", name, "and i am ", age , "years old and i live in ",city)
#greet("Ravi", "25")

#here we didnt return age so we didnt get age in output whatever the arguments we gave in function we shoul return it so that it print in outpput
#def greet(name, age ):
 #   return f"my name is {name}"
    
#msg = greet("ravi", 25)
#print(msg)
#Learn about variable scope (local vs global variables)?

#Start with Python lists?
#local variable
#def colour():
 #   color = "blue"
  #  print(color)
    
#colour()
#globalll variable
#language = "python"
#def lang():
 #   print("i am learning", language)
    
#lang()
#city = "Delhi" #global variable if we want to use this variable in function we should use global keyword
#def cou():
    
 #   country = "india" #local variable
  #  print("my country is :", country)
   # print("my city is :", city)
#cou()
#list
#fruits = ["Apple", "bananana", "Cherry"]
#fruits[0] = "Mango"
#fruits.append("Grapes")
#fruits.remove("bananana")
#fruits.pop()
#print(fruits)
#fruits = ["Apple", "Bananna", "cheery"]
#print(fruits)
#numbers = [10,25, 7, 18,35, 25] #find max number in list
#res = max(numbers)
#print(res)
#num =[1,2, 3]
#res = len(num)
#print(res)
#word = ["madam", "in", "madam"]
#rev = word[::-1]
#print(rev)
#if rev == word:
 #  print("it is  a palindrome:",word)
#items = [1, 2, 2, 3, 4, 4, 5]
#newli = []
#for i in items:
 #  if i not in newli:
  #    newli.append(i)
#print(newli)
#num = [1, 2, 3, 4]
#res = 1
#for i in num:
 #  res = res * i
#print(res)
#square = [1,2,3,4,5]
#res = []
#for i in square:
 #  square_num = i * i
  # res.append(square_num)
#print(res)
#num = [10,20,30,40,50]
#num.remove(max(num))
#second_largest = max(num)
#print(second_largest)
#for i in range(1):
 #  for j in range(1,4):
  #     print("*", "*", "*")
#for i in range(1,4):
 #  for j in range(1,11):
  #    print(i, "*", j, "=" ,i*j)
   #   print()
#for i in range(1,5):
 #  for j in range(i):
  #     print(j+1, end ='')
   #print()

#for i in range(1,8):
 #  if i == 1:
  #    print("*", end ='')
   #elif i == 2:
    #  continue
   #elif i == 3:
    #  print("*","*","*", end ='')
   #elif i == 4:
    # continue
   #elif i == 5:
    #   print("*","*","*","*","*", end ='')
   #elif i == 6:
    #  continue
   #elif i == 7:
    #   print("*","*","*","*","*","*","*", end ='')
               
   #print()
#for i in range(1, 8, +2):
 #  for j in range(1, i+1):
  #    print("*", end ='')
   #print()
#for i in range(1, 8, 2):  # i = 1, 3, 5, 7
 #      spaces = (7 - i) // 2
  #     print(" " * spaces, end='')
   #    print("*" * i)

#for i in range(1, 5):#Task 1: Right-Angled Triangle of Numbers
 #     for j in range(1, i+1):
  #       print(j, end ='')
   #   print()
#Task 2: Inverted Star Triangle
#for i in range(6, 0 ,-1):
 #  for j in range(1, i):
  #     print("*", end ='')
   #print()
#Task 3: Multiplication Table (1 to 3)
#for i in range(1,4):
 #  for j in range(1, 11):
  #    print(i ,"*", j, "=", i*j)
   #print()
#for i in range(1,5):
 #    if i % 2 == 0:
  #      print(" ", end ='')
   #  for j in range(1, 5):
    #      print("#", end ='')
     #print()

#for i in range(1, 5):
 #   spaces = (5- i)//2
  #  print(" " * spaces, end ='')
   # for j in range(1, i+1):
    #    print(j, end ='')
    #for j in range(i -1, 0, -1):
     #  
      #   print(j, end ='')
    #print()
#tuples
#numbers = (1, 3, 5, 3, 7, 3, 9)
#print(numbers.count(3))
#colors = ('red', 'blue', 'green', 'blue', 'yellow')
#print(colors.index("blue"))
#t1 = (3, 4, 5)
#t2 = (3, 4, 6)
#print((1, 2, 3) == (1, 2, 3))  # True
#print((3, 4, 5) < (3, 4, 6))   # True
#print((3, 4, 5) > (3, 4, 6))
#tupple unppacking
#person = ("John", 30, "USA")
#name, age, country = person
#print("name")
#print("age")
#print("country")
#sets
#a = {10, 20, 30}
#a.add(40)
#a.remove(20)
#a.discard(50)
#print(a)
#a = {1, 2, 3, 4}
#b = {3, 4, 5, 6}
#print(a.union(b))
#a = {1, 2, 3, 4}
#b = {3, 4, 5, 6}
#print(a.symmetric_difference(b))not common in both a and b
#a = {1, 2, 3, 4}
#b = {3, 4, 5, 6}
#print(a.intersection(b))which is common in both a and b
#a = {1, 2, 3, 4}
#b = {3, 4, 5, 6}
#print(a.difference(b)) num which in a not in b
#class_A = {"Ravi", "Kiran", "Sneha", "Arjun"}
#class_B = {"Sneha", "Ravi", "Anjali", "Vikram"}
#print(class_A or class_B)
#dictionaries
"""
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
book.pop("price")
print(book.items())
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
print(book.keys())
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
print(book.values())

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
print(book.items())
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
print(book.get("price"))

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
book.update({"pages" : "450"})
print(book.items())
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "price": 299
}
book.pop("price")
print(book.items())
"""
"""
marks = {
   "math" : 90,
   "science" : 85,
   "English" : 88
}
marks.update({"History" : 75})
marks.update({"science" : 89})
marks.pop("English")
print(marks.keys())
print(marks.values())
print(marks.items())
"""
#sentence = "python is awesome"
#print(sentence.capitalize())#first letter upper case rest lower case
#print(sentence.count("s"))
#print(sentence.title())#make first letter in every word upper case
#print(sentence.startswith("python"))
"""
full_name = "ravi kumar"
print(full_name.title().startswith("Ravi"))

print(full_name.split())
"""

"""
data = "abc123"
print(data.isalnum())
print(data.isdigit())
print(data.isalpha())
"""
"""
text = "  I love apples. Apples are tasty.  "
print(text.replace("apples", "mangoes"))
print(text.strip())
"""
"""
colors = "red,blue,green"
print(colors.split())  #it takes space as a default separator
print(colors.split(","))

colors_list = colors.split(",")
print("-".join(colors_list))
"""
#word = "PythonRocks"
#print(word[1:7:2])#strat:stop:step it means it picks every second charcter strts from inde 1 to eculsvie 7 means 6
#otpu:ptoRcs
#text = "Programming"
#print(text[:6])
#escape chracters
"""
Name = "Ravi"
Subject = "Python"
Score= 95
print("Name:", Name, /n"Subject:", Subject, /n"Score:", Score))
print("she said, python is fun")
#print("she said, \"python is fun\"") this will pint with double quotes
print("C:\\Users\\ravi")
"""
#f string .format()
"""
name = "ravi"
score = 92
print(f"Hello {name} your scored {score} in python")
"""
#Welcome Sneha! Your balance is ₹500.00
"""
name = "sneha"
balance = 500.00
print("Welcome {}!, your balance is {}".format(name, balance))
"""
#Name     Marks
#Ravi     90
#Sneha    88
"""
print(f"{'Name':<10}{'marks'}")
print(f"{'Ravi':<10}{90}")
print(f"{'sneha':<10}{50}")
"""
#list comprehensions

#for i in range(1,6):
 #   square = i * i
  #  print(square)
#below code is list comprehensions
#square = [i*i for i in range(1,6)]
#print(square)
#list = [1,2,3,4,5,6]
#for i in list:
 #   if i % 2 == 0:
  #      print(i)
#even = [i for i in list if i %2 ==0]
#print(even)
"""
list = ["apple", "cherry","banana"]
upper_case = [i.upper() for i in list]
print(upper_case)
"""
"""
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i > 3:
        i = i * i* i
        print(i)
"""
#using list compprehensions print cube of numbers that greater than 3
"""
numbers = [1, 2, 3, 4,5]
newlist = [i*i*i for i in numbers if i > 3]
print(newlist)
"""
#list comprhension sqaure of numbers from 1 to 10
#squares = [i*i for i in range(1,11)]
#print(squares) 
"""
nums = [1, 4, 7, 10, 15, 18, 21]
even = [i for i in nums if i % 2==0]
print(even)
"""
"""
words = ["python", "is", "awesome"]
new = [i[:1] for i in words ]

print(new)
"""
"""
nums = [2, 4, 6, 8, 10]
greater = [i for i in nums if i > 5]
print(greater)
"""
"""
fruits = ["apple", "banana", "cherry"]
new_list = [len(i) for i in fruits]
print(new_list)
"""
#nested list comprehensions
"""
matrix = []
for i in range(4):
    row = []
    for j in range(1,4):
        row.append(1)
    matrix.append(row)
print(matrix)

matrix = [[1 for i in range(4)] for j in range(1,5)]
print(matrix)
"""
"""
matrix = []
for i in range(3):
    r1 = []
    
    for j in range(3):
        if i == 0:
            r1.append(j+1)
        if i == 1:
            r1.append(j + 3)
        if i == 2:
            r1.append(j + 6)
    matrix.append(r1)
    
print(matrix)
"""
#dictonary comprehensions
"""

nums = {1:1, 2:2, 3:3, 4:4, 5:5}
squares = {k:v**2 for k, v in nums.items()}
print(squares)
"""
#names = ["Ram", "Lakshman", "Sita", "Ravi"]
#for i in names:
    
 #   if len(i) > 4:
  #      print(i,":", len(i))
#names = ["Ram", "Lakshman", "Sita", "Ravi"]
#new = {i:len(i) for i in names  if len(i) > 4}  
#print(new)

#students = {'Ravi': 70, 'Kiran': 85, 'Sneha': 90, 'Arjun': 40}
#new = {}
"""
for key,value in students.items():
    if value >= 80:
        new[key] = value 
print(new)
"""
#new_dict ={v:k for k, v in students.items() if v >=80} 
#print(new_dict)
"""
book = {
    "title": "Python 101",
    "author": "Guido",
    "pages": 250
}

print(book["title"])
"""
"""
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}
new_dict = {}
for key,value in fruits.items():
    new_dict[value] = key
new_dict = {v:k for k, v in fruits.items()}#thsi dictnry comprehension oneline
print(new_dict)
"""

"""
nums = {
    1: "one",
    2: "two",
    3: "three"
}
new_nums = {}
for key, value in nums.items():
    new_nums[value] = key
    
new_nums ={v:k for k, v in nums.items()}
print(new_nums)
"""
"""
nested dictonary
students = {
    "ravi": 82,
    "kiran": 74,
    "sneha": 91,
    "arjun": 67,
    "meena": 88
}
new_students = {}

for key,value in students.items():
      if value > 75:
          new_students[key.upper()] = value
print(new_students)

new_students = {k.upper():v for k , v in students.items() if v >75}
print(new_students)
"""
"""
employees = {
    "ravi" :{"age":26,"dep":"manufacture","salary":30000},
    "sneha":{"age":22,"dep":"testing","salary":26000},
    "arjun":{"age":24,"dep":"HR","salary":20000}
}
new_dict = {}
for name,details in employees.items():
      if details["salary"] > 25000:
          new_dict[name] = details["dep"]
print(new_dict)
"""
#students["ravi"]["english"] = 88
#print(students["ravi"]) 
"""
from enum import NAMED_FLAGS


employees = {
    "ravi": {"salary": 30000, "bonus": 2000},
    "sneha": {"salary": 28000, "bonus": 2500},
    "arjun": {"salary": 25000, "bonus": 1500}
}

"""
"""
new_dict = {}
for key, details in employees.items():
    inner = {}
    for k,v in details.items():
        inner[k] = v + 1000
        new_dict[key] = inner
        
print(new_dict)
"""
#nested sictonary comprhensipn
"""
new_dict = {
    key: {k: v + 1000 for k, v in details.items()}
    for key,details in employees.items()
}
print(new_dict)
"""
#new_dict = {key:details["salary"] + 1000 for key, details in employees.items()}
#print(new_dict)

"""
marks = {
    "ravi": {"math": 85, "science": 78},
    "sneha": {"english": 90, "math": 88}
}

new_dict = {}
for key,details in marks.items():
    inner = {}
    for k, v in details.items():
        inner[k.upper()] = v
    new_dict[key] = inner
 """
"""
new_dict = {
    key: {k.upper(): v for k, v in details.items()}
    for key, details in marks.items()
}
print(new_dict)
"""
#enumerate
"""
fruits = ["apple", "banana", "mango", "orange"]
for index, fruit in enumerate(fruits, start = 1):
    print(index,fruit)
"""
"""
students = ["ravi", "sneha", "arjun", "meena"]
for Roll_no, student in enumerate(students, start = 101):
    print(Roll_no, student)
"""
"""
nums = [10, 15, 22, 33, 40, 55]
for index,num in enumerate(nums, start = 0):
    if index % 2 == 0:
        print(index,num)
"""
"""
colors = ["red", "blue", "green", "yellow"]
new_dict = {}
for index,color in enumerate(colors, start=0):
    new_dict[index] = color
print(new_dict)
"""
"""
students = ["ravi", "sneha", "arjun"]
marks = [85, 92, 78]
for student,mark in zip(students,marks):
    print(student,mark)
"""
"""
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "dark red"]
new_fruits = {}
for fruit,color in zip(fruits,colors):
    new_fruits[fruit] = color
print(new_fruits)
"""
"""
first_names = ["John", "Jane", "Alice"]
last_names = ["Doe", "Smith", "Brown"]
for k,v in zip(first_names, last_names):
    print(k,v)
"""
"""
a = [10, 20, 30]
b = [1, 2, 3]
for k,v in zip(a,b):
    c = k + v
    print(k, "+", v, "=",c)
"""
#*args and **kwargs
"""
def sum_all(*args):
    t =0
    for i in args:
        t = t + i
    return t
        
print(sum_all(10, 20, 30))
print(sum_all(5,5,5,5,5))
"""
#3, 8, 2, 10, 6
""""
def find_max(*args):
    n = max(args)
    return n
print(find_max(3, 8, 2, 10, 6))
"""
"""
def greet(**kwargs):
    if "name" in kwargs:
        print(f"hello, {kwargs['name']}")
    else:
        print("hello guest")
greet(name="sneha")
greet(age=24)
           # Output: Hello!
"""
"""
def show_details(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

show_details(10, 20, name="Meena", city="Delhi")
"""
"""
num = [3,8,2,10,6]
min_num = num[0]
for i in num:
    if i < min_num:
        min_num = i
print(min_num)
"""
"""
def multiply_all(*args):
      mul = 1
      for i in args:
        mul = mul *i
      return mul
    
print(multiply_all(2,3,4))
print(multiply_all(2,3,5))
"""
"""
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)

print_info(name="Ravi", age=25, city="Hyderabad")
"""
"""
def total_marks(name, *marks):
    t = 0
    for i in marks:
       t = t + i
    print(name, t)
total_marks("sneha", 80,90,85)
"""
#lambda functions
"""
nums = [1,2,3,4,5]
squares = list(map(lambda  x:x*x, nums))
print(squares)
"""
"""
nums = [10, 15, 22, 33, 40, 55]
odd = list(filter(lambda x:x % 2 != 0, nums))
print(odd)
"""
"""
a = [5, 10, 15]
b = [1, 2, 3]
element = list(map(lambda a,b: a + b, a,b))
print(element)
"""
"""
names = ["ram", "sita", "hanuman"]
con = list(map(lambda x: x.upper(), names))
print(con)
"""
"""
names = ["Ravi", "Sneha", "Arjun", "Meena", "Om"]
length = list(filter(lambda x : len(x) > 4, names))
print(length)
"""
"""
words = ["hello", "", "world", "", "python"]
filtered =list(filter(lambda x: x != "", words))
print(filtered)
"""
"""
nums = [5, 12, 7, 18, 21]
eve_odd = list(map(lambda x: x % 2 == 0, nums))
print(eve_odd)
"""
"""
nums = [10, 20, 30]
ind_add = list(map(lambda x :x[0] * x[1], enumerate(nums)))
print(ind_add)
"""
"""
names = ["Arjun", "Ravi", "Anu", "Meena", "Amit"]
strtl = list(filter(lambda x: x[0] == "A", names))
print(strtl)
"""
"""
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
li = list(map(lambda x: x[0] + x[1],zip(list1,list2)))
print(li)
"""
#recursion
"""
def down(n):
    if n == 0:
         return
    print(n)
    down(n-1)
    
down(10)
"""
"""
def fact(n):
     if n == 1:
         return 1
     return n * fact(n-1)
print(fact(5))
"""

"""
def sum(n):
    if n == 1:
         return 1
    return n + sum(n-1)
print(sum(4))
"""
#read and writing files
"""
with open("first.txt", "w") as file:
    file.write("Hello, this is my first file")
"""
"""
with open("first.txt", "r") as file:
    data = file.read()
    print(data)
"""
"""
with open("first.txt", "a") as file:
    file.write("\n this is my new project")
with open("first.txt", "r") as file:
    for line in file:
        print(line.strip())
"""
#deleting a file
"""
import os

if os.path.exists("first.txt"):
    os.remove("first.txt")
    print("file successfully deleted")
else:
    print("file does not exist")
"""
#csv files
"""
import csv

with open("students.csv", mode ="w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["ravi", 25, "hyderbad"])
    writer.writerow(["tej", 28, "bang"])
"""
"""
import csv

with open("students.csv", mode = "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""
"""
import os

filename = "students.csv"
if os.path.exists(filename):
    os.remove(filename)
    print("deleted successfully")
else:
    print("file doesnot exists")
"""
#CSV with Dictionaries

"""
import csv

with open("data.csv", mode ="w", newline ="") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "age", "city"])
    writer.writeheader()
    writer.writerow({"name": "Ravi", "age": 25, "city": "Hyderabad"})
    writer.writerow({"name": "Sneha", "age": 23, "city": "Mumbai"})





import csv
with open("data.csv", mode = "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
"""
#task1 txtfiles
"""
with open("notes.txt", "w", newline ="") as file:
    file.write("Today I learned file handling" "\n It's really useful in Python")
with open("notes.txt", "r") as file:
    for line in file:
        words = line.split()
        print("total words:",len(words))
"""
"""
import csv

with open("student.csv", mode ="w", newline ="") as file:
    writer = csv.writer(file) 
    
    writer.writerow(["name", "age", "grade"])
    
    writer.writerow(["ravi", 20, "A"])
    writer.writerow(["sneha", 22, "B"])
    writer.writerow(["arjun", 21, "A"])
with open("student.csv", mode ="r") as file:
    reader = csv.reader(file)
    next(reader) #skip the first row
    for row in reader:
        if row[2] == "A":
        
           print(row[0],row[2])
"""
"""
with open("file.txt", "w") as file:
    file.write("hello, this is my project")
with open("file.txt", "r") as file:
    for line in file:
        print(line)
"""
#copying files
"""
with open("file.txt", "r") as src:
    content = src.read()
with open("file1.txt","w")as dest:
    dest.write(content)
    print(content)
with open("file.txt", "r") as src,  open("file1.txt", "w") as dest:
    for line in src:
        dest.write(line)
"""
"""
with open("notes.txt", "w") as file:
    file.write("Python is easy to learn" "\n File handling is useful in python" "\n Practice daily")
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
"""
"""

try:
    n1 = int(input("Enter numerator"))
    n2 = int(input("Enter denominator"))
    total= n1/n2
    print(total)
except ZeroDivisionError:
    print("denominator should not be zero")
"""
"""
try:
    num = int(input("Enter a number"))
    print(num)
except ValueError:
    print("num shoulld not be string")
"""
"""
try:
    f = open("file.txt", "r") 
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file does not exist")
    
"""
"""
try:
    n = int(input("Enter anum"))
    t = 100/n
    print(t)
except ValueError:
    print("num should not be string")
except ZeroDivisionError:
    print("denominator should not be zero")
"""
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result is:", result)
finally:
    print("Program finished.")
"""
"""
while True:
    try:
        a = int(input("Enter a numerator"))
        b = int(input("Enter a denominator"))
        res = a/b
    except ValueError:
        print("invalid input, enter num")
    except ZeroDivisionError:
        print("denominator should not be zero")
    else:
        print("result", res)
        print("opperation complte")
        break
"""
"""
for attempt in range(3):  # attempt will be 0, 1, 2
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
    except ZeroDivisionError:
        print("Cannot divide by zero.\n")
    else:
        print("Result:", result)
        print("Operation complete.")
        break  # exit loop if successful
else:
    print("❌ Too many invalid attempts. Exiting.")
"""
#age = int(input("Enter your age: "))
#assert age >= 0, "Age must be non-negative"
#print("Valid age:", age)
"""
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
print("Age is valid:", age)
"""
"""
n = int(input("enter a num"))
if n > 10:
    raise ValueError("num is greater than ten")
print(n)
"""
"""
passwrd = str(input("enter your password"))
res = len(passwrd)
if res < 6:
    raise ValueError("password is shorten")
print("logged in")
"""
"""
age = int(input("Enter your age"))
assert age <= 100, "Age should belwo 100"
    
print("your age is" , age)
"""
"""
import random

n = random.randint(1, 10)
guess = int(input("enter a num"))
if guess == n:
    print("guess is correct")
else:
    print("incoreect guess", n)
"""
"""
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print(f"What is {num1} × {num2}?")

answer = int(input("Your answer: "))

if answer == num1 * num2:
    print("✅ Correct!")
else:
    print(f"❌ Incorrect. The correct answer is {num1 * num2}")
"""
"""
import math
n = int(input("enter a num"))
area = math.pi * math.pow(n, 2)
print("area of the circel", area)
"""
"""
import math
num = float(input(("enter a num")))
print("ceiling value", math.ceil(num))
print("floor value", math.floor(num))
"""
"""
import random
names = ["ravi", "sneha", "arjun", "meena"]
winner = random.choice(names)
print(winner)
"""
"""
n = int(input("enter a num:"))
for i in range(1, 11):
    print(n, "*", i, "=", n*i)
"""
"""
import datetime
currentdate = datetime.datetime.now()
print("currentdate and time:", currentdate)
"""
"""
import datetime
currentdate = datetime.date(2025, 6,10)
#print("current date:", currentdate)
"""
"""
import datetime
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%A"))
"""
"""
import datetime
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days =1)
print("tomorrow", tomorrow)
yesterday = today - datetime.timedelta(days =1)
print("yesterday", yesterday)
"""
"""
import datetime
today = datetime.date.today()
birthdate = today + datetime.timedelta(days = 50)
daysleft = birthdate - today
print(daysleft)
"""
"""
import datetime
now = datetime.datetime.now()
currentime= now.strftime("%I:%M %p")
print(currentime)
"""
"""
import datetime
today = datetime.datetime.now()
futurtime = today + datetime.timedelta(days = 5, hours = 3)
print(futurtime.strftime("%d/%m/%Y %I:%M %p"))
"""
"""
from mymath import add, greet

print(add(10,5))
print(greet("tejaswi"))
"""
#import mymath as mm
#print(mm.add(10,5))
#OOPS
#classes and objects
"""

class animal:
    def __init__(self, name, species,sound,age,color):
        self.name = name
        self.species = species
        self.sound = sound
        self.age = age
        self.color = color

    def describe(self):
        print(f"This is a {self.species} named {self.name}")
    def make_sound(self):
        print(f"Hi, my name is {self.name} and i say {self.sound}")

a1 = animal("Tommy", "dog","bowbow","5","black")

a1.describe()
a1.make_sound()
a2 = animal("kitten","cat", "meow meow","2", "white")
a2.describe()
a2.make_sound()
"""
#inheritance 
#it allows achild calss or subclass User the properties and methods of a parent class or superclass.
"""
class Animal:
    def __init__(self, name, age, color, species,sound):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.sound = sound
    def describe(self):
        print(f"my name is {self.name} and i am {self.age} i am {self.color} and i am {self.species}")
    def make_sound(self):
        print(f"my name is {self.name} and i say {self.sound}")

class dog(Animal):
    def fetch(self):
        print(f"{self.name} loves fetching the ball!")
class cat(Animal):
    def climb(self):
        print(f"{self.name} loves climbing the trees!")
a1 = Animal("Tommy", "4","BLACK","dog","bowbow")
a1.describe()
a1.make_sound()

a2 = dog("lucky", "3", "brown", "dog", "bowbow")
a2.fetch()
a2.make_sound()

a3 = cat("kitten", "2", "white", "cat", "meow meow")
a3.describe()
a3.make_sound()
"""


#method overiding
"""
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def describe(self):
        print(f"my name is {self.name}")

class bird(Animal):
    def describe(self):
        print(f"i am {self.name} and i sound {self.sound}")
a1 = Animal("tommy", "bowbow")
a1.describe()
a2 = bird("parrot", "Tweet Tweet")
a2.describe()
"""
#super()
"""
class Animal:
    def __init__(self, name,sound):
        self.name = name
        self.sound = sound
    def describe(self):
        print(f"my name is {self.name}")
        
class dog(Animal):
    def describe(self):
      super().describe() #calling parent class method
      print(f"my name is {self.name} and i say {self.sound}")
        
a1 = dog("tommy", "bowbow")
a1.describe()
"""
"""
class Pet:
    def __init__(self, name, age):
        print("pet constructor called")
        self.name = name
        self.age = age
    def show_info(self):
        print("Name:", self.name, "age:", self.age)
class cat(Pet):
    def __init__(self, name , age, color):
        print("cat constructor called")
        self.color = color
        super().__init__(name,age)
    def show_info(self):
        super().show_info()
        print("color:",self.color)

c1 = cat("kitty","3", "white")
c1.show_info()
"""
#encapsulation geter and setter metods
"""
class Student:
      def  __init__(self, studentname,marks):
            self.studentname = studentname
            self.__marks = marks
      def set_marks(self, newmarks):
         if newmarks <= 100:
              self.__marks = newmarks
         else:
              print("your failed")
      def get_marks(self):
         return self.__marks
m1 = Student("ravi", 55)
m1.set_marks(101)
print(m1.get_marks())
"""
"""
class Account:
    def __init__(self, balance):
        
        self.__balance = balance#private variable
    def set_acc(self, amount):
        
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("invalid amount")
    def get_acc(self):
        return self.__balance
a1 = Account(3000)
a1.set_acc(2000)
print(a1.get_acc())
"""
#pollymorphism
"""
class Parrot:
    def speak(self):
        print("parrot says squak")
class Cow:
    def speak(self):
        print("cow says ambaa")
class Duck:
      def speak(self):
          print("duck syas quack quack")
   
for animal in (Parrot(), Cow() ,Duck()):
    animal.speak()
"""
"""

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def describe(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Buddy says: woof")
    def describe(self):
        print(f"Buddy is a playful {self.name}")
class Cat(Animal):
    def speak(self):
        print("whiskers says: meow")
    def describe(self):
        print(f"whiskers is a fluffy {self.name}")
class Duck(Animal):
    def speak(self):
        print("daisy says: quack")
    def describe(self):
        print("daisy love water")

animals = [Dog("dog"), Cat("cat"), Duck("duck")] #Create objects with names
for animals in animals:
    animals.speak()
    animals.describe()
"""
#giving name dynaimcally while creating objects
"""
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    def speak(self):
        pass
    def describe(self):
        pass
class Lion(Animal):
    def speak(self):
        print(f"{self.name} says: {self.sound}")
    def describe(self):
        print(f"{self.name} is the king of the jungle")
class Elephant(Animal):
    def speak(self):
        print(f"{self.name} says : {self.sound}")
    def describe(self):
        print(f"{self.name} has long ears and big tears")
class Monkey(Animal):
    def speak(self):
        print(f"{self.name} says: {self.sound}")
    def describe(self):
        print(f"{self.name} is playful and loves ananas")
animals = [Lion("simba","lion", "rora"), Elephant("appu", "elephat", "prr"), Monkey("chimpu", "monkey","ohh ahh ohh ahh")]
for animal in animals:
    animal.speak()
    animal.describe()
"""
#__str__() is called automatically when you do print(object)

#Without __str__(), it prints the memory address like <__main__.Book object at 0x...>


"""
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def __str__(self):
              return (f"{self.title} directed by {self.director} in the {self.year}")
m1 = Movie("Interstellar", "Christopher Nolan", 2014)
print(m1)
"""
#school_name = class variable = common for all students

#name, grade = instance variables = different for every student
"""
class Book:
    library_name = "City Central Library" # class variable
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_info(self):
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print("library:", b1.library_name)
        
b1 = Book("the girl in 105 room", "chetanbagat")


b1.show_info()
"""
#magic method  __add and __eq
"""
class Money:
    def __init__(self, rupees):
        self.rupees = rupees
    def __add__(self, other):
       return Money(self.rupees + other.rupees)
    def __str__(self):
        return (f"{self.rupees}")
m1 = Money(100)
m2 = Money(200)
m3 = m1 + m2
print(m3)
"""
#__eq__()
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Creating two books
b1 = Book("Python", "Ravi")
b2 = Book("Python", "Ravi")
b3 = Book("Java", "Sneha")

print(b1 == b2)  # True (same title and author)
print(b1 == b3)  # False
"""
#for i in range(10, 0, -1):
  #  print(i)
"""
marks = [65, 89, 45, 90, 55]
marks.sort()#ascending order
#marks.sort(reverse = True)#descending order
print(marks)
"""
"""
new_dict=[]
def count_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            new_dict.append(number)
    print(len(new_dict))
res = count_odd(numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
#tuple unpacking
"""
person = ("Ravi", 25, "Hyderabad")
name, age, city = person
#name = "Ravi"
#age = 25
#city = "Hyderabad"
print(name, age, city)
"""
#count vowels in a string
"""
name = "Tejaswi"
vowels = "aeiou"
new_list = []
for i in name:
    if i in vowels:
        new_list.append(i)
print(len(new_list))
"""
#palindrome
"""
name = str(input("enter a name:"))
new_name = name[::-1]

if new_name == name:
    print("it is palindrome")
else:
    print("it is not a palindrome")
"""
#list comprehensions
"""
names = ["ravi", "sneha", "arjun"]
upper = [i.upper() for i in names]
print(upper)
"""
#isdigit()
"""
text = "H3ll0 Pyth0n 2025"
new = [i for i in text if i.isdigit()]
print(new)
"""
#words = ["hello", "python", "world"]
#revverse = [ i[::-1] for i in words ]
#print(revverse)
#nested comprehnsion
#flattened 2D list
"""
matrix = [[1, 2], [3, 4], [5, 6]]
new = [num for row in matrix for num in row]
print(new)
"""
"""
star = [["*" for i in range(6)]  for j in range(6)]
for row in star:
    print(" ".join(row))
"""
#odd = [x*x for row in [[1,2,3,],[4,5,6]] for x in row if x%2!=0]
#print(odd)
"""
words = ["apple", "banana", "grape"]
vowels = "aeiou"
new = [j for i in words for j in i if j in vowels]
print(new)
"""
"""
names = ["ravi", "sneha", "arjun"]
age =[2,3,4]
for name, age in zip(names,age):
     print(name,age)
"""
"""
num = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x:x % 2 == 0, num))
print(even)
"""
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"my name is{self.name} and i am {self.age} yesras old")
    def greet(self):
        print("hello welcome")
p1 = Person("ravi", 25)
p1.show_info()
p1.greet()
"""
"""
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    @classmethod
    def from_string(cls, data_string):
        brand, year = data_string.split(",")
        return cls(brand, int(year))
        
c1 = Car.from_string("Honda, 2019")
c2 = Car.from_string("Hyundai, 2018")
print(f"brand: {c1.brand} year: {c1.year}")
print(f"brand: {c2.brand} year: {c2.year}")
"""
"""
class Book:
       total_books = 0
       def __init__(self, title, authour):
           self.title = title
           self.authour = authour
           Book.total_books = Book.total_books +1
       @classmethod
       def get_book(cls):
          return cls.total_books
       def show_info(self):
           return(f"Title: {self.title} authour:{self.authour}")
b1 = Book("Harry Potter" ,"J.K. Rowling")
b2 = Book("The Alchemist" ,"Paulo Coelho")
print(Book.get_book())
print(b1.show_info())
print(b2.show_info())
"""

"""
new = []
def view_tasks():
    for index,task in enumerate(new, start =1):
        print(index, task)
view_tasks()
def add_tasks():
    while True:
        your_tasks = input("Add your tasks:" )
        
        if your_tasks == "exit":
            break
        new.append(your_tasks)
    print("Task added succesfully")
    print("your tasks are:" )
    for index,new_one in enumerate(new, start =1):
        print(index, new_one)
add_tasks()
def tasks_done():
    done_tasks = input("enter your task numbers as (comma-seperated):")
    numbers = done_tasks.split(",")
    for num in numbers:
        if num.strip().isdigit():
            index = int(num.strip())
            if 1 <= index  <= len(new):
                print(f"task  {new[index -1]} as done")
            else:
                print("invlid num")
        else:
            print("out of range")
                
tasks_done()
"""

    
          

        



    







    
    


    