#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    return 'Access granted' if (username == 'ADMIN' or username == 'admin') and password == '12345' else 'Access denied'

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    mod_3 = num % 3
    mod_5 = num % 5
    if mod_3 == 0 and mod_5 == 0:
        return 'FizzBuzz'
    elif mod_3 == 0:
        return 'Fizz'
    elif mod_5 == 0:
        return 'Buzz'
    else:
        return num

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None
