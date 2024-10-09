#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

from fibonnaci import generate_fibonacci
import argparse
import sys

def prime_number(x):
    if x <= 1:
        return False
    if x == 2: 
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True
    
def largest_prime(limit):
    fibonnaci_list = generate_fibonacci(limit) # gen fib numbers to the limit
   
    prime_fib_num = [] # empty list to hold prime fibonnaci numbers

    for num in fibonnaci_list:
        if prime_number(num): # check if the fib number is prime
            prime_fib_num.append(num) # if the number is prime, add it to the list

    if prime_fib_num:
        return max(prime_fib_num) # return largest prime fib number
    else:
        return None
    
if __name__ == "__main__":
    # parse command line argument
    parser = argparse.ArgumentParser(description = "Find  largest prime Fibonacci number below limit.")
    parser.add_argument("limit", type = int, help = "Upper limit for Fibonacci numbers")
    args = parser.parse_args()

    result = largest_prime(args.limit)

    if result:
        print(f"The largest prime Fibonacci number under {args.limit} is: {result}")
    else:
        print(f"No prime Fibonacci numbers found under {args.limit}.")


