#!/usr/bin/python
import sys
import re
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		id_, title, tagnames, author_id, body, node_type, parent_id, abd_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
		#print body
		mots= re.findall(r"[\w']+", body)
		#print mots
		#print "*************************"
		for mot in mots:
			#print mot
			#print "***"
			print "{0}\t{1}".format(mot, id_)

