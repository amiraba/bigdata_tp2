#!/usr/bin/python
import sys
occTotal = 0
oldKey = None
ids=[]

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisId = data
	
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}:\t{2}".format(oldKey,occTotal,ids)
		occTotal = 0
		del ids[:]
	oldKey = thisKey
	ids.append(thisId)
	occTotal += 1

if oldKey != None:
	print oldKey,"\t", occTotal,"\t:",ids

