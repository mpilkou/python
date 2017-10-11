#!/usr/bin/python3 

import os

file = open("text_12.txt", "w+", 1)

print(file.name)
print(file.closed)
print(file.mode)

file.write("aabbcc\naabb\naa")

print(file.read(10))

print("Position: ", file.tell())
file.seek(0,0) # $2 => 0-start, 1-current, 2-end (text file)

# read by char
file.seek(0,0)
text = ""
while True:
	ch = file.read(1)
	if not ch:
		break
	text += ch
	print(ch)

print(text)

print("Position: ", file.tell())
file.seek(0,0)
print(file.read(10))

os.rename("text_12.txt","text_12_1.txt")
os.remove("text_12_1.txt")

os.mkdir("./newdir")
os.chdir("./newdir")
print(os.getcwd())
os.chdir("..")
os.rmdir("./newdir")

file.close()
