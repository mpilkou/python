#!/usr/bin/python3 
print("1---------------------")
# class
class Animal:
	"basic class"
	pops_count = 0
	
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		Animal.pops_count += 1

	def print_count(self):
		print("Total pops: %d" % Animal.pops_count)

	def print_animal(self):
		print("Name: ", self.name, "\n\t Kind: ", self.kind)

# main
# init
a1 = Animal("Gadia","Zlopopuszka")
a2 = Animal("Pops","Gerakakl")
a3 = Animal("Gadia","Nifertitia")

a1.print_animal()
a2.print_animal()
a3.print_animal()

print("Total %d" % Animal.pops_count)

print("2---------------------")
# manipulations
print(a2.kind)
print("_1_")
print(hasattr(a2, "kind"))    		# Returns true if attribute exists
print("_2_")
print(getattr(a2, "kind"))    		# Returns value of attribute
print("_3_")
print(setattr(a2, "kind", "007")) 	# Set attribute 
print("_4_")
print(delattr(a2, "kind"))	    	# Delete attribute

print("3---------------------")
# class atrib
print ("A.__doc__:", Animal.__doc__)
print ("A.__name__:", Animal.__name__)
print ("A.__module__:", Animal.__module__)
print ("A.__bases__:", Animal.__bases__)
print ("A.__dict__:", Animal.__dict__ )


print("garbage")
print("4---------------------")
#	garbage collection
a = 40      # Create object <40>
print("1:   a: ",a)
b = a       # Increase ref. count  of <40> 
c = [b]     # Increase ref. count  of <40> 
print("1:   c: ",c)

del a       # Decrease ref. count  of <40>
print("2:   b: ",b,"\tc:",c)
b = 100     # Decrease ref. count  of <40> 
c[0] = -1   # Decrease ref. count  of <40> 
print("2:   b: ",b,"\tc:",c)

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3));   # prints the ids of the obejcts
del pt1
del pt2
del pt3

print("5---------------------")
# class inheritance
class Parent:		# define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)


class Child(Parent): 		# define child class
   def __init__(self):
      super().__init__()
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
# class C(A, B): // subclass of A and B

print("6---------------------")
# overloading methods

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

print("7---------------------")
# data hiding
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)
print (counter._JustCounter__secretCount)

print("8---------------------")

class Word1():
	def __init__(self,text):
		self.text = text

class Word2():
	def __init__(self,text):
		self.text = text
	def __eq__(self,outher):
		return self.text.lower() == outher.text.lower()
	def __str__(self):
		return self.text
	def __repr__(self):
		return "Word is ",self.text," :-)"

first = Word1('ha')
first	# <__main__.Word1 object at 0x1006ba3d0> 
print (first)

second = Word2('ha')
second	# "Word is ha :-)"
print (second)
