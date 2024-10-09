#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def generate_fibonacci(limit):
	fibonacci_numbers = [0 ,1]

	while fibonacci_numbers[-1] + fibonacci_numbers[-2] < limit:
		num = fibonacci_numbers[-1] + fibonacci_numbers[-2]
		fibonacci_numbers.append(num)
		
	return (fibonacci_numbers)

if __name__ == "__main__":
	result = generate_fibonacci(100)

with open("fibonnaci_100.txt", 'w') as file:
	print(f"The fibonacci numbers under 100:{generate_fibonacci(100)}", file = file)




