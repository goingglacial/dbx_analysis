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

def parse_field_items(field_names, arbitrary_list):
    '''
    Given the field names in a dictionary nested in an arbitrary list,
    print the field items (values for respective keys in dictionaries).
    Flatten lists and convert all field items to lowercase. 
    '''
    # must get all of the values for a given field name
    for field_name in field_names:
        field_content = [dictionary[field_name] for dictionary in arbitrary_list]
        field_content_list = flatten(field_content)
        # field_content_lowercase = [x.lower() for x in field_content_list]
        category_field_items = []
        for x in field_content_list:
            if x is not None:
                category_field_items.append(x)
    return category_field_items

def print_field_content(field_names, arbitrary_list):
    '''
    Print out all field names followed by colon and all field items for that category.
    '''
    # pass in parse_field_items function to make this more concise
    for field_name in field_names:
        category_field_items = parse_field_items(field_names, arbitrary_list)
        print field_name + ":" + ", ".join(str(x) for x in category_field_items) + "."

if __name__ == '__main__':
    main()


'''
TODO

apply counter for each field name
for each field name, write to csv file for that field

ideal CSV format:

hobbies.csv

hiking 3 
biking 2

'''