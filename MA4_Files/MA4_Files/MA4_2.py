#!/usr/bin/env python3

from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(1)
	print(f.get())
	print(f.fib())
	f.set(6)
	print(f.fib())
if __name__ == '__main__':
	main()
