#!/usr/bin/python
import sys
import re
for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) == 5: #users file
		user_ptr_id, reputation, gold, silver, bronze=data
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_ptr_id, reputation, gold, silver, bronze, "u")

	if len(data) == 19:
		id_, title, tagnames, author_id, body, node_type, parent_id, abd_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(author_id, id_, title, tagnames, node_type, parent_id, abd_parent_id, added_at, score,"n")



