#!/usr/bin/python3

def fun1 (str):
	"Print string"
	print (str)
	return

def fun2 (name, age):
	"Print name, age"
	print ("name: %s, age: %i" %(name,age))
	return

def fun3 (str = "STRING!!!"):
	"print"
	print (str)
	return

def fun4 (*args):
	"Arguments"
	print("SYSO:")
	for i in args:
		print (i)
	return

sum = lambda arg1, arg2: arg1 + arg2

total = 20;
def fun5 (arg1, arg2):
	total = arg1+arg2
	return total

fun1("Call")
fun2(age = 12, name="AAA")
fun3()
fun4(10, 20, 30)
fun4(sum(10,30))
print("Global:", total)
print("SUM: ", fun5(20,20))
