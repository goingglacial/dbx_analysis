#!/usr/bin/env python
from collections import Counter
from compiler.ast import flatten

import csv
import itertools
import json
import sys

def main():

    script, filename = sys.argv

    people_list = json.load(open(filename, 'r'))
    arbitrary_list = people_list['users']
    field_names = parse_field_names(arbitrary_list)

    # for each field name in the array of field names...
    for field_name in field_names:
        # yield field items for each field name
        category_field_items = parse_field_items(field_name, arbitrary_list)
        # count occurrences of field items for each field name
        field_items_ranked = compute_field_item_count(field_name, category_field_items, arbitrary_list)
        # for each field name, write field items and respective counts to individual csv file
        write_to_csv(field_name, field_items_ranked, arbitrary_list)

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

def parse_field_items(field_name, arbitrary_list):
    '''
    Given a field name (key for a person dictionary), return
    the field items (values) for that particular field name.

    RIGHT NOW: Loops over all the field names and for each them, gets all the
    values and combines into one list.
    '''

    # field_names = parse_field_names(arbitrary_list)
    field_content = [p[field_name] for p in arbitrary_list]
    category_field_items = []
    field_items_list = flatten(field_content)

    for x in field_items_list:
        if x is not None:
            category_field_items.append(x)

    return category_field_items

def compute_field_item_count(field_name, category_field_items, arbitrary_list):
    '''
    For each field name, compute occurrences of field items within
    that category.
    '''   
    field_items_ranked = Counter(category_field_items)
    return field_items_ranked

def write_to_csv(field_name, field_items_ranked, arbitrary_list):
    '''
    For each field name, write a CSV with field items and 
    count of field items.
    '''
    writer = csv.writer(open('dbx.csv', 'wb'))
    # dict.items() returns (key, value) tuples
    for key, value in field_items_ranked.items():
        writer.writerow([key, value])

if __name__ == '__main__':
    main()