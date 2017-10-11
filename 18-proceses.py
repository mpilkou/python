#!/usr/bin/python3
import os

print(os.getpid())
print(os.getcwd())

print(os.getuid())
print(os.getgid())



import subprocess

print(subprocess.getoutput('date'))

print(subprocess.getstatusoutput('date'))

# rerurn = 0
print(subprocess.call('date'))

# multiprocessing
import multiprocessing
import os
def do_this(what):
	whoami(what)
def whoami(what):
	print("Process %s says: %s" % (os.getpid(), what))
if __name__ == "__main__":
	whoami("I'm the main program")
	for n in range(4):
		p = multiprocessing.Process(target=do_this("I'm function %s" % n))
		#p = multiprocessing.Process(target=do_this,args=("I'm function %s" % n,))
		p.start()


# terminate
import multiprocessing
import time
import os
def whoami(name):
	print("I'm %s, in process %s" % (name, os.getpid()))
def loopy(name):
	whoami(name)
	start = 1
	stop = 1000000
	for num in range(start, stop):
		print("\tNumber %s of %s. Honk!" % (num, stop))
		time.sleep(1)
if __name__ == "__main__":
	whoami("main")
	p = multiprocessing.Process(target=loopy, args=("loopy",))
	p.start()
	time.sleep(5)
	p.terminate()

