#!/usr/bin/env python3

"""
Rosalind: IEV
https://rosalind.info/problems/iev/

For a random variable X taking integer values between 1 and n, the expected
value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking
the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large
number of rolls, we should expect to obtain an average of 3.5 on the die (even
though it's not possible to roll a 3.5). The formula for expected value confirms
that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally
spaced outcomes has the same probability is called a uniform random variable
(in the die example, this "equal spacing" is equal to 1). We can generalize our
die example to find that if X is a uniform random variable with minimum possible
value a and maximum possible value b, then E(X)=a+b2. You may also wish to
verify that for the dice example, if Y is the random variable associated with
the outcome of a second die roll, then E(X+Y)=7.

Given: Six nonnegative integers, each of which does not exceed 20,000. The
integers correspond to the number of couples in a population possessing each
genotype pairing for a given factor. In order, the six given integers represent
the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.

Sample Dataset

1 0 0 1 0 1

Sample Output

3.5
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
        couples = [int(couple) for couple in dataset_file.read().split()]

    print(f'Couple data: {couples}')

    # probabilities of each position, by punnet square
    # AA-AA, 4/4
    # AA-Aa, 4/4
    # AA-aa, 4/4
    # Aa-Aa, 3/4
    # Aa-aa, 2/4
    # aa-aa, 0/4

    probabilities = [1, 1, 1, 0.75, 0.5, 0]

    # element-wise multiplication of the probabilities for each couple
    couple_probabilities = [a_val*b_val for a_val,
                            b_val in zip(couples, probabilities)]

    # print(couple_probabilities)

    # sum total probability of dominant
    sum_probs = sum(couple_probabilities)

    # multiply by number of offspring
    sum_probs *= 2

    print(sum_probs)


if __name__ == "__main__":
    main()
