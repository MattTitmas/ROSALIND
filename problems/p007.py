from itertools import product

# https://rosalind.info/problems/iprb/

def main():
    with open('data/p007.txt', 'r') as f:
        data = [int(i) for i in f.readline().split()]

    # Homozygous dominant = data[0]
    # Heterozyguous = data[1]
    # Homozygous recessive = data[2]
    markers = ['BB', 'Bb', 'bb']
    relate = {
        'BB': 0,
        'Bb': 1,
        'bb': 2
    }

    total_prob = 0
    for i in markers:
        for j in markers:
            copy = data[:]
            total = sum([1 if 'B' in i else 0 for i in list(product(i, j))])

            prob_1 = copy[relate[i]] / sum(copy)
            copy[relate[i]] = max(0, copy[relate[i]] - 1)
            prob_2 = copy[relate[j]] / sum(copy)

            total_prob += prob_2 * prob_1 * (total/4)
    return total_prob


if __name__ == '__main__':
    print(main())
