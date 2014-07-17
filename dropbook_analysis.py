#!/usr/bin/env python
from collections import Counter
from compiler.ast import flatten

import itertools
import json
import sys

script, filename = sys.argv

people_list = json.load(open(filename, 'r'))

# make array with all values for key 'hobbies' in dropbook dicts
hobbies = [p['hobbies'] for p in people_list['users']]

# render one list with all hobbies listed, print in lowercase so we can group duplicates
hobbies_list = flatten(hobbies)
hobbies_lowercase = [x.lower() for x in hobbies_list]

# remove duplicate hobbies to ascertain correct count of hobbies listd by Dropboxers
def remove_duplicates(l):
    return list(set(l))
remove_duplicates(hobbies_lowercase)

# call function on hobbies_lowercase
merged_dropbook_hobbies = remove_duplicates(hobbies_lowercase)

# print all_dropbook_hobbies: flattened, lowercase, dupes merged

total_hobbies_count = len(merged_dropbook_hobbies)
print "SF Dropboxers boast a whopping " + str(total_hobbies_count) + " hobbies! Yeehaw!"

all_dropbook_hobbies_listed = hobbies_lowercase
all_dropbook_hobbies_listed

# count number of times each hobby is listed as such by Dropboxers
hobbies_by_count = Counter(all_dropbook_hobbies_listed)
hobbies_by_count
'''
Go back to this and print in different format ('vertical', CSV-type list).
'''

# count top ten most common hobbies among Dropboxers
hobbies_ranked = Counter(all_dropbook_hobbies_listed).most_common(10)
top_ten = [x[0] for x in hobbies_ranked]
print "The top ten most popular hobbies at Dropbox HQ are: "
for hobby in top_ten:
    print hobby

# print the top hobby among SF Dropboxers
print "The most popular hobby at Dropbox is " + top_ten[0] + "."