#!/usr/bin/python3

# if / else
if True:
	print ("True")
elif False:
	print ("ELIF")
else:
	print ("False")

# while // TRUE == 1
val = 1
while not val == 0:
	val = int(input("Your number: "))
	print ("Entered: ", val)
else:
	print ("Last wariable is", val)

# for
for letter in "Python":
	print ("Letter:	", letter)
	continue
print()

pass #	"I do't write code for a moment"

fruts = ["banana", "apple", "mango"]

for frut in fruts:
	print("FRUT: ",frut)
	break
