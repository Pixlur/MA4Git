#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	fibpy = []
	fibnum = []
	fibc = []
	n = [x + 30 for x in range(16)]
	"""
	for x in n:
		start = pc()
		fib_py(x)
		end = pc()
		fibpy.append(end-start)
	for x in n:
		start = pc()
		fib_numba(x)
		end = pc()
		fibnum.append(end-start)
	"""
	for x in n:
		start = pc()
		f = Person(x)
		f.fib()
		end = pc()
		fibc.append(end-start)
	"""
	plt.plot(n ,fibpy)
	plt.plot(n ,fibnum)
	"""
	plt.plot(n ,fibc)
	plt.savefig("plots.svg")
if __name__ == '__main__':
	main()
