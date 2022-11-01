from functools import reduce
from math import comb

# https://rosalind.info/problems/lia/

def ind_prob(n, k, p=.25):
    return (comb(n, k)) * (p ** k) * (1 - p) ** (n - k)


def main():
    with open('data/p015.txt', 'r') as f:
        k, n = [int(i) for i in f.readline().split(' ')]

    prob = 0
    for i in range(n, (2 ** k) + 1):
        prob += ind_prob((2 ** k), i)
    return prob


if __name__ == '__main__':
    print(main())
