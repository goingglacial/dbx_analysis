#!/usr/bin/env python
from collections import Counter
from compiler.ast import flatten

import itertools
import json
import sys

def main():

    script, filename = sys.argv

    people_list = json.load(open(filename, 'r'))
    arbitrary_list = people_list['users']

    parse_field_names(arbitrary_list)

    # print_field_items(field_names, arbitrary_list)

def parse_field_names(arbitrary_list):
    '''
    Given the field names in a dictionary, returns those field names. 
    '''
    field_names = set()
    for arbitrary_dict in arbitrary_list:
        for key in arbitrary_dict.keys():
            field_names.add(key)
    print "The field names are as follows: " + ", ".join(str(x) for x in field_names) + "."

def print_field_values(field_names):
    


if __name__ == '__main__':
    main()

'''
def print_field_items(field_names, arbitrary_list):
    
    Given the field names in an arbitrary list, prints the top-n most frequently
    occurring items for each field.
  
    for field_name in field_names:
        print "The items for " + field_name + " are: "

def compute_top_n(field_name, arbitrary_list, n): 
   
    Given the name of a field in a particular list, computes top ten most frequently
    occurring items for that field.
    

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













for each field name, print out all values 
for each field name, write to csv file for that field

ideal CSV format:

hobbies.csv

hiking 3 
biking 2

organization.csv

tuck shop 50
engineering 40
design 20

etc.
'''






