#!/usr/bin/python3

import support1_10, math as mat

from support2_10 import fun2	# use import * // for import all
Money = 20

def AddMoney(i):
	global Money
	Money = Money + i

support1_10.fun1("AHAHAHAHHAHA")
print(fun2(2,3))
print(__name__)

print(Money)
AddMoney(10)
print(Money)

print(dir(mat))

print()
print(globals())
print()
print(locals())
print()
#print(keys())
#reload(math)
