#!/usr/bin/env python3

"""
Rosalind: REVP
https://rosalind.info/problems/revp/

A DNA string is a reverse palindrome if it is equal to its reverse complement.
For instance, GCATGC is a reverse palindrome because its reverse complement is
GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.

Sample Dataset:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

__author__ = "weightedEights"
__version__ = "0.1"
__license__ = "MIT"

import sys

def main():
    # check arguments for proper usage
    if len(sys.argv) != 3:
        print(f'Usage: ./prtm.py <path/mass table> <path/dataset>')
        exit(1)

    # read in data set and..
    dataset = ""

    # alphabet as dictionary, key:value as symbol:weight
    weighted_alphabet = {}

    with open(sys.argv[2], 'r') as dataset_file, open(sys.argv[1], 'r') as mass_table_file:
        # handle the dataset string
        for line in dataset_file:
            dataset = str(line.strip())

        # handle the mass_table
        for line in mass_table_file:
            # print(line.split(' '))
            # append dictionary, cast value as float for later math
            weighted_alphabet[line.split(' ')[0]] = float(line.split(' ')[3].strip())

    # work on the dataset
    # print(f'Alphabet: {weighted_alphabet}')
    dataset_weight = 0

    # print(f'Dataset: {dataset}')
    for char in dataset:
        # print(f'Symbol, Weight: {char}, {weighted_alphabet[char]}')
        dataset_weight += weighted_alphabet[char]

    print(f'Weight: {dataset_weight}')


if __name__ == "__main__":
    main()
