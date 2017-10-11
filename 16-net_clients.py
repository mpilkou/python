#!/usr/bin/python3

import urllib.request as ur
url = 'http://beta.speedtest.net/'
conn = ur.urlopen(url)
data = conn.read()
print("connection:\t",conn)
print("data:\t\t%s" %data[1:50], end="...\n")
print("connect stat:\t",conn.status)
print("Content-Type:\t",conn.getheader('Content-Type'))

#same
#for key,val in conn.getheaders():
#	print(key,val)

for i in conn.getheaders():
	#print(i[0],i[1]) - same
	print(i)



import requests
url = 'http://beta.speedtest.net/'
resp = requests.get(url)
print(resp)
