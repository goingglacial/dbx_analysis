#!/usr/bin/env python

import json
from collections import Counter
from compiler.ast import flatten
import itertools

people_list = json.load(open('dropbook_output.json', 'r'))

# make array with all values for key 'hobbies' in dropbook dicts
hobbies = [p['hobbies'] for p in people_list['users']]

# render one list with all hobbies listed, print in lowercase to merge dupes
hobbies_list = flatten(hobbies)
all_dropbook_hobbies = [x.lower() for x in hobbies_list]

total_count = len(all_dropbook_hobbies)
print "SF Dropboxers boast a whopping " + str(total_count) + " hobbies! Sick brah!"

# count ten most popular hobbies among SF dropboxers
hobbies_ranked = Counter(all_dropbook_hobbies).most_common(10)
top_ten = [x[0] for x in hobbies_ranked]

print "The ten most popular hobbies at Dropbox are:"
for hobby in top_ten:
    print hobby

print "The most popular hobby at Dropbox is " + top_ten[0] + "."