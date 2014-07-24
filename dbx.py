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
    parse_field_items(field_names, arbitrary_list)

def parse_field_names(arbitrary_list):
    '''
    Given a list of dictionaries nested in a list, returns
    the keys from each of the dictionaries, where keys are
    field names.
    '''
    field_names = set()
    for arbitrary_dict in arbitrary_list:
        for key in arbitrary_dict.keys():
            field_names.add(key)
    return field_names

def parse_field_items(field_names, arbitrary_list):
    '''
    Given a field name (key for a person dictionary), return
    the field items (values) for that particular field name.
    '''
    # field_names = parse_field_names(arbitrary_list)
    for field_name in field_names:
        field_content = [p[field_name] for p in arbitrary_list]
        category_field_items = []
        field_items_list = flatten(field_content)

        for x in field_items_list:
            if x is not None:
                category_field_items.append(x)
        return category_field_items

def compute_field_item_count(field_name, arbitrary_list):
    '''
    Given the name of a field in a particular list, counts the 
    number of times that field items occur within that category.
    '''    
    # get count for items
    # field_items_counted = Counter(all_field_items)
    # return field_items_counted


if __name__ == '__main__':
    main()