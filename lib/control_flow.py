#!/usr/bin/env python3
def admin_login(username, password):
    # your code here
    if username == "sudo" and password == "12345":
        return "Access denied"
    elif username == "ADMIN" or username == "admin" and password == "12345":
        return "Access granted"
    elif username != "admin" or password != "12345":
        return "Access denied"
    
    
admin_login("sudo", "12345")
admin_login("admin", "12345")
admin_login("ADMIN", "12345")
admin_login("admin", "sudo")


def hows_the_weather(temperature):
    # your code here
    if temperature < 40 :
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return"It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return"It's perfect out there!"
hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)
        
""""
Write a function fizzbuzz() takes in a number. For multiples of three, return "Fizz" instead of the number. 
For the multiples of five, return "Buzz". For numbers which are multiples of both three and five, return "FizzBuzz". For all other numbers, just return the number itself.
"""
def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 5 == 0 and num % 3 != 0 :
        return ("Buzz")
    elif num % 5 == 0 and num % 3 == 0 :
        return "FizzBuzz"
    else:
        return num
fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)

fizzbuzz(15)
     
"""
Write a function calculator() that takes three arguments: an operation and two numbers.
 If the operation is one of the following: +, -, *, or /, return the value of calling the operation on the two numbers. 
 Otherwise, output a message saying "Invalid operation!" and return None.
"""

def calculator(operation, num1, num2):
    # your code here
    if operation == "+" :
        return num1 + num2
    elif operation == "-":
        return num1 - num2 
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
    
calculator("+", 1, 1)
calculator("-", 3, 1)
calculator("*", 3, 2)
calculator("/", 4, 2)
calculator("nope", 4, 2)
