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
    if len(sys.argv) != 2:
        print(f'Usage: ./revp.py <path/dataset>')
        exit(1)

    # read in data set
    dataset = ""

    with open(sys.argv[1], 'r') as dataset_file:
        # handle the dataset string
        # for line in dataset_file.read():
            # dataset will end up as the last line of the file
            # dataset = str(line.strip())

        dataset = dataset_file.read()[14:].replace('\n', '')
        # print(dataset)

    # work on the dataset
    return_list = []

    # print(f'Dataset: {dataset}')
    # iterate over the whole string, from 0 to end-3
    # print(f'dataset: {dataset[0:len(dataset)-3]}')
    for i in range(0, len(dataset)-3):
        # for each position, check ahead 4, 6, 8, 12 positions (inefficient)
        for j in range(i+4, i+12+1, 2):
            # print(f'{dataset[i:j]}, {check_rev_palindrome(dataset[i:j])}')
            if j <= len(dataset):
                if check_rev_palindrome(dataset[i:j]):
                    print(f'i={i} to j={j}, {dataset[i:j]}')
                    return_list.append((i+1, len(dataset[i:j])))
                    # stop checking this range of j
                    # break

    # format the return tuples
    # print("\n".join([' '.join(map(str, r)) for r in return_list]))

    # write return list for submission
    for result in return_list:
        # print(f'{result[0]} {result[1]}')
        with open("result.file", 'a') as fout:
            fout.write(f'{result[0]} {result[1]}\n')


def check_rev_palindrome(string_in):
    # check if input string is a reverse palindrome
    # create a translation map, since we also swap the same symbols
    swap_table = string_in.maketrans("ATCG", "TAGC")

    # check if palindrome
    # return string_in == string_in[::-1]

    # reverse, then check if palindrome
    return string_in == string_in[::-1].translate(swap_table)


if __name__ == "__main__":
    main()
