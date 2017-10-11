#!/usr/bin/python3
import time;

tic = time.time()
print ("Time:",tic);
print ("Local:",time.localtime());
print ("Local:",time.asctime(time.localtime(time.time())));
print ("Start: %s" % time.ctime())
time.sleep(5)
print ("End: %s" %time.ctime())
