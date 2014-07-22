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

    parse_field_names(arbitrary_list)
    print_field_item_count(field_names, arbitrary_list)

def parse_field_names(arbitrary_list):
    '''
    Given a list of dictionaries nested in a list, returns
    the keys from each of the dictionaries.
    '''
    field_names = set()
    for arbitrary_dict in arbitrary_list:
        for key in arbitrary_dict.keys():
            field_names.add(key)
    return field_names
    # print " ,".join(str(x) for x in field_names)

def print_field_item_count(field_names, arbitrary_list):
    for field_name in field_names:
        all_field_items = compute_field_item_count(field_name, arbitrary_list)
        print field_name + ":" + " ,".join(str(x) for x in all_field_items)

def compute_field_item_count(field_name, arbitrary_list):
    '''
    Given the name of a field in a particular list, computes
    top ten most frequently occurring items for that field.
    '''
    # get all of the values for a given field_name
    field_content = [p[field_name] for p in arbitrary_list]

    all_field_items = []
    field_content_list = flatten(field_content)
    for x in field_content_list:
        if x is not None:
            all_field_items.append(x)

    return all_field_items
    # get count for items
    # field_items_counted = Counter(all_field_items)
    # return field_items_counted



'''
        field_item_count = compute_field_item_count(field_name, arbitrary_list)
    print field_name + ":" + " ,".join(str(x) for x in field_item_count)
'''

if __name__ == '__main__':
    main()