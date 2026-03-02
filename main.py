"""Simple demo module for Fibonacci.

Provides a straightforward recursive implementation of Fibonacci numbers.

Functions
---------
fib(n):
	Return the n-th Fibonacci number where fib(0) == 0 and fib(1) == 1.

When run as a script, prints fib(0..10).
"""

import sys


def fib(n: int) -> int:
	"""Return the n-th Fibonacci number (recursive).

	Parameters
	- n: non-negative integer

	Returns
	- int: the n-th Fibonacci number

	Raises
	- ValueError: if n is negative
	"""
	if n < 0:
		raise ValueError("n must be non-negative")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)


def _demo():
	# Print the first 11 Fibonacci numbers
	for i in range(11):
		print(f"fib({i}) = {fib(i)}")


if __name__ == "__main__":
	# If a single integer argument is provided, print fib for that value.
	if len(sys.argv) == 2:
		try:
			n = int(sys.argv[1])
		except ValueError:
			print("Please provide an integer.")
			sys.exit(1)
		try:
			print(fib(n))
		except ValueError as e:
			print(e)
			sys.exit(1)
	else:
		_demo()
