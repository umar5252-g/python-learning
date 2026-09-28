# print("hello world")
# firstName = input("enter your first name: ")
# lastName = input("enter your last name: ")
# print(firstName,     lastName)
# height = "1.85m"
# age = 53

# name = input("enter the name of the super hero")
# print (height)
# print(age)
# print(name, 'is secretly a superhero')

# a = int(input("enter a: "))
# b = int(input("enter b: "))

# sum = a+b

# print("sum: ",sum)


# build a calculator that can perform following operations
# num1 = int(input("enter first number: "))
# op= input("enter operation u want to perform: ")
# num2 = int(input("enter second number:"))

# if op == '+' : 
#   print(num1+num2)
# elif op == '-' :
#   print(num1-num2)
# elif op == '/':
#   print(num1/num2)
# elif op == '*':
#   print(num1*num2)

# for i in range(1, 20,2):
#   print(i)
  
  # table of 57

# for i in range(57, 571, 57):
#   print(i)
  
# for i in range(3, 51, 3):
#   if i == 15: 
#     continue
#   print(i)

# num1 = 3
# num2 = 5

# for i in range(1, 1001):
#   if i %num1== 0 and i%num2 == 0 :  
#     print(i)
#     break

# list tuple set dictionary 
# list is mutable it has insert slice etc functions
# tuple is immutable is is fast also tuple values cannot be changed
# set is the collection of unique elements 
# dictionary is the collection of key value pair
# module are the collection of related functions , bundles and classes etc

# ok so slicing work on tupple as well
# marks = 87,78, 79,89,98
# marks[5] = 34 --> this assigment operation is not possible in tuple
# print(type(marks))

# ok so if we do for example 45 in marks and print it if the value is present it will give us true else it will give us false

# marks = [45,75,45,75,56,75,65]
# marks.append(7)

# print(75 in marks)
# for score in marks: 
#   print(score)

# marks = {"maths": 78, "english": 98, "physics": 78}
# marks["chemistry"] = 75
# print(marks)

# for key in marks: 
#   print(key, marks[key])

#set
# marks = {89, 98, 89, 89, 89, 34}
# marks[0] = 34
# print(marks)
## so in list we have append insert clear slicing etc these kind of features but in tupple we cant insert a value because tupple is immutable

# def sum(a, b):
#   print(a+b)

# sum(19,11)

# import random
# print(random.random())
# print()

# numbers = {101, 105, 102, 108, 101, 105, 110}
# for score in numbers: 
#   print(score)

# records = [
#   (101, 'alice', 50000),
#   (102, 'bob', 40000),
#   (103, 'charlie', 30000),
# ]

# empId = int(input("enter the empoylee ID: "))
# for record in records: 
#   if empId == record[0] :
#     print("name: ", record[1])
#     print("salary: ", record[2])

# print(len([1,3,4,6,7]))
# print(max([1,3,5,4,6]))
# print(min((3,4,6,23,2)))

# import math 
# print(dir(math))
# from math import sqrt
# print(sqrt(16))

# import random
# print(random.randint(1,10))


# def oddOreven (num):
#   if num %2 == 0:
#     print("even")
#   else:
#     print("odd")  

# oddOreven(2)    

# def prime(num):
#   if(num %num == 0 and num & 1== num): 
#     print("prime")

def guessGame(num):
  if(num>35):
    print("You guess a high number")
  elif(num<35):
    print("You guess a low number")
  else :
    print("congratulations dude! you guess the right number ") 

guessGame(int(input("guess the number: ")))    