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
    field_names = parse_field_names(arbitrary_list)

    parse_field_items(field_names, arbitrary_list)
    print_field_content(field_names, arbitrary_list)

def parse_field_names(arbitrary_list):

    '''
    Given the field names in a dictionary, returns those field names. 
    '''
    field_names = set()
    for arbitrary_dict in arbitrary_list:
        for key in arbitrary_dict.keys():
            field_names.add(key)
    return field_names
    # print "The field names in " + " are as follows: " + ", ".join(str(x) for x in field_names) + "."

def parse_field_items(field_names, arbitrary_list):
    '''
    Given the field names in a dictionary nested in an arbitrary list,
    print the field items (values for respective keys in dictionaries).
    '''
    # must get all of the values for a given field name
    for field_name in field_names:
        field_content = [dictionary[field_name] for dictionary in arbitrary_list]
        all_field_items = []
        field_content_list = flatten(field_content)
        for x in field_content_list:
            if x is not None:
                all_field_items.append(x)
    return all_field_items

def print_field_content(field_names, arbitrary_list):
    '''
    Print out all field names followed by colon and all field items for that category.
    '''
    for field_name in field_names:
        field_content = [dictionary[field_name] for dictionary in arbitrary_list]
        print field_name

if __name__ == '__main__':
    main()


'''
TODO

for each field name, write to csv file for that field

ideal CSV format:

hobbies.csv

hiking 3 
biking 2

'''