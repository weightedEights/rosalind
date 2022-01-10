#!/usr/bin/env python3

"""
Rosalind: MRNA
https://rosalind.info/problems/mrna/

For positive integers a and n, a modulo n (written amodn in shorthand) is the
remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and
division with respect to the modulo operation. We say that aand b are congruent
modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then
a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may
wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very
large) integer solution modulo a smaller number to avoid the computational
pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the
stop codon in protein translation.)

Sample Dataset:
MA

Sample Output:
12

Hint:
What does it mean intuitively to take a number modulo 1,000,000?
"""

__author__ = "weightedEights"
__version__ = "0.1"
__license__ = "MIT"

import sys

def main():
    # check arguments for proper usage
    if len(sys.argv) != 2:
        print(f'Usage: ./mrna.py <path/dataset>')
        exit(1)

    # read in data set
    dataset = ""

    with open(sys.argv[1], 'r') as dataset_file:
        # handle the dataset string

        dataset = dataset_file.read().strip()
        print(dataset)


if __name__ == "__main__":
    main()
