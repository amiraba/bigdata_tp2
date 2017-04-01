#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		id_, title, tagnames, author_id, body, node_type, parent_id, abd_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
		if  "!" in body[:-1] or  "?" in body[:-1] or "." in body[:-1]:
			pass
		else:
			print "{0}\t{1}".format(id_,body)
		

