#!/usr/bin/env python3

"""
Rosalind: PRTM
https://rosalind.info/problems/prtm/

In a weighted alphabet, every symbol is assigned a positive real number called a
weight. A string formed from a weighted alphabet is called a weighted string,
and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet
is the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. (Consult the monoisotopic mass table.)

Sample Dataset:
SKADYEK

Sample Output:
821.392
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


    # alphabet as dictionary, key:value as symbol:weight
    print(f'Name of script: {sys.argv[0]}')
    print(f'Arg1: {sys.argv[1]}')


if __name__ == "__main__":
    main()
