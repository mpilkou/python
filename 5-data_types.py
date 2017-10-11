#!/usr/bin/python3

#	variables
a = b = c = 1		# declare variables s1

a,b,c = 1,"hello",'a'	# declare variables s2

del a,b,c 		# delete variable

str = "hello"

print (str[1:1:3], str[2:],str*2, 'h' in str)
print (str.capitalize())
print (str.center(20, 'a'))
#print (str.encode('base64','strict'))
#print (str.decode('base64','strict'))
print ("My %s kg %d" %("Zara",89.9))
print (str.isdecimal())

#	lists
list1 = ["abc", 7, 3.14]
list2 = ["alf", "agent", "pi"]

print (list1[1:3],"\n", list2[2:],"\n",list1[-2],"\n", list1 + list2, "\n", list1*2)

#	tuples
tuple1 = ('abc', 7, 3.14)
tuple2 = ("alf", "agent", "pi")

print (tuple1[1:3],"\n", tuple2[2:],"\n", tuple1 + tuple2, "\n", tuple1*2)

# valid / invalid
# tuple1 [2] = 10 	# invalid
list1 [2] = 10 		# valid

print (tuple1[2], list1[2])

# 	dictionary
dic1 = {}
dic1["one"] = "first"
dic1[2] = "second"

dic2 = {"name":"Gadia", "sername":"Gadiewna"}

print (dic1["one"], dic1[2])
print (dic2.keys(), dic2.values())
