#!/usr/bin/python3

# errors

# example
def KelToFar(Temp):
	assert(Temp >= 0), "Colder than absolute zero!"
	return ((Temp-273)*1.8)+32

print (KelToFar(273))
print (int(KelToFar(507.35)))
#print (KelToFar(-7))

# 1
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

# 2
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers:\n\t", Argument)

# Call above function here.
temp_convert("xyz")


# 3
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])

# 4
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e.args)
