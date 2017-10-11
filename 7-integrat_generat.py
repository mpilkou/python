#!/usr/bin/python3
import sys

print("SYS argv",sys.argv)
# iterator
list = [1,2,3,4]
it = iter(list)
print(next(it),"  ",next(it),end="\n")

for i in it:
	print (i," ",end="\n")

print()
it = iter(list)

while True:
	try:
		print(next(it))
	except StopIteration:
		#sys.exit()
		break

# generator
def fib (n):
	a,b,c = 1,1,0
	while True:
		if(c > n):
			return
		yield a
		a, b = b, a+b
		c += 1
f = fib(5)

while True:
	try:
		print(next(f),end=" ")
	except StopIteration:
		sys.exit()
