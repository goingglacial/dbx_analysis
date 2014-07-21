#!/usr/bin/env python
from collections import Counter
from compiler.ast import flatten

import itertools
import json
import sys

def main():

    script, filename, n = sys.argv

    people_list = json.load(open(filename, 'r'))
    arbitrary_list = people_list['users']
    field_names = parse_field_names(arbitrary_list)  

    print_top_n(field_names, arbitrary_list, int(n))

def parse_field_names(arbitrary_list):
    field_names = set()
    for arbitrary_dict in arbitrary_list:
        for key in arbitrary_dict.keys():
            field_names.add(key)
    return field_names

def print_top_n(field_names, arbitrary_list, n):
    '''
    Given the field names in an arbitrary list, prints the top-n most frequently
    occurring items for each field.
    '''
    for field_name in field_names:
        top_n_field_values = compute_top_n(field_name, arbitrary_list, n)
        print "The top " + str(n) + " values for " + field_name + " are: ", top_n_field_values

def compute_top_n(field_name, arbitrary_list, n): 
    '''
    Given the name of a field in a particular list, computes top ten most frequently
    occurring items for that field.
    ''' 

    # getting all of the values for a given field_name
    field_content = [p[field_name] for p in arbitrary_list]

    all_field_items = []
    field_content_list = flatten(field_content)
    for x in field_content_list:
        if x is not None:
            all_field_items.append(x)

    # getting count for items and getting the top ten most frequently occurring
    field_items_ranked = Counter(all_field_items).most_common(n)

    top_n = [x[0] for x in field_items_ranked]
    return top_n

if __name__ == '__main__':
    main()


# for each field name, print out all values 
# for each field name, write to csv file for that field
# hobbies.csv, etc. 
# remove n value scheme