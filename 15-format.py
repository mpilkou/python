#!/usr/bin/python3


place = 'caf\u00e9'
print(place)
print(type(place))
plase_bytes = place.encode("utf-8")
print(plase_bytes)
print(type(plase_bytes))

print("%s" % 7.03)
print("%f" % 7.03)
print("%e" % 7.03)
print("%g" % 7.03)
print("%10d" % 17.13)
print("%.10d" % 17.13)
print("%d%%" % 7.03)


import re
source = 'Young Frankenstein'
# martch - begin
# . - {1}
# * - {0...}
m = re.match('You', source) # 
if m:
	print(m.group())
m = re.match('^You', source) # begin
if m:
	print(m.group())
m = re.match('.*Frank', source) # search
if m:
	print(m.group())

# search - at all the text
m = re.search('Frank', source) 
if m:
	print(m.group())

# findall - many words in text
m = re.findall('n', source) 
print(m)
m = re.findall('n.', source) 
print(m)
m = re.findall('n?', source) 
print(m)
m = re.findall('n.?', source) 
print(m)

# split
m = re.split('n', source) 
print(m)

# sub ~= replase (shablons / strings)
m = re.sub('n','?', source)
print(m)


m = re.findall('^n|ou', source) 
print(m)

source = '''I wish I may, I wish I might ... Have a dish of fish tonight.'''

# I wish	(find I before wish) 
m = re.findall('I (?=wish)', source)
print(m)

# find wish after I
m = re.findall('(?<=I) wish', source)
print(m)
