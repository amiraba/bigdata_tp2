#!/usr/bin/python
import sys
oldKey = None
theList=[]
lista=[]
lista2=[]
mydict = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		user_ptr_id, reputation, gold, silver, bronze, u=data
		mydict = {'user_ptr_id': user_ptr_id, 'reputation': reputation, 'gold': gold, 'silver': silver, 'bronze': bronze, 'u':u}
		lista.append(mydict)

#sys.stdin.flush()

#for line in sys.stdin:
#	data = line.strip().split("\t")
	else:
		if len(data) ==10:
			#print "{0}".format("*********")
			author_id, id_, title, tagnames, node_type, parent_id, abd_parent_id, added_at, score, n =data

			if oldKey and oldKey !=author_id:
				lista2[:]=[]
				#mydict={}

			oldKey=	author_id	

			mydict2 = {'author_id': author_id, 'id_': id_, 'title': title, 'tagnames': tagnames, 'node_type': node_type, 'parent_id': parent_id, 'abd_parent_id': abd_parent_id, 'added_at': added_at, 'score': score,'n':n }
			lista2.append(mydict2)
			theList.append(lista2)
			#mydict2 = {'user_ptr_id': user_ptr_id, 'reputation': reputation, 'gold': gold, 'silver': silver, 'bronze': bronze, 'u':u}
			#any(d['user_ptr_id']==author_id for d in lista)
			#for d in lista:
				#print "{0}".format(author_id)
				#print "{0}\t{1}".format(d.get("user_ptr_id"), author_id)
				#if author_id==d.get("user_ptr_id"):
					#print "{0}".format("----")
					#print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id_, title, tagnames, author_id, node_type, parent_id, abd_parent_id, added_at, score, d.get('reputation'), d.get('gold'), d.get('silver'), d.get('bronze') )


for l,k in zip(theList,lista):
	for d in l:
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format( d['id_'], d['title'], d['tagnames'], d['author_id'],d['node_type'], d['parent_id'], d['abd_parent_id'], d['added_at'], d['score'] ,k['reputation'], k['gold'], k['silver'], k['bronze'] )

