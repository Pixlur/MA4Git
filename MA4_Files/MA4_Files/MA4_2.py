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
	#fibc = []
	n = [x + 20 for x in range(11)]
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
	f = Person(47)
	print(f.fib()) #-1323752223 overflow

	plt.plot(n ,fibpy, label = "Python")
	plt.plot(n ,fibnum, label = "Numpy")
	#plt.plot(n ,fibc, label = "c++")
	plt.xlabel("n:te termen i fibonacci serien")
	plt.ylabel("tid(s)")
	plt.legend(loc='best')
	plt.savefig("plots2.svg")
if __name__ == '__main__':
	main()
