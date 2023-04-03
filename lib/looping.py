#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)

    print("Happy New Year!")

def square_integers(int_list):
   return [i_number ** 2 for i_number in int_list]

def fizzbuzz():
    for numbers in range(1, 101):
        if not numbers % 15:
            print("FizzBuzz")
        elif not numbers % 5:
            print("Buzz")
        elif not numbers % 3:
            print("Fizz")
        else:
            print(numbers)
