#!/usr/bin/python
import sys
salesTotal = 0
nbTotal = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		moy = salesTotal/nbTotal
		print "{0}\t{1}".format(oldKey,moy)
		salesTotal = 0
		nbTotal = 0
	oldKey = thisKey
	salesTotal += float (thisSale)
	nbTotal += 1

if oldKey != None:
	print oldKey,"\t", salesTotal/nbTotal

