from itertools import product

# https://rosalind.info/problems/prot/

def main():
    with open('data/p008.txt', 'r') as f:
        line = f.readline()[:-1]
        data = [line[i:i+3] for i in range(0, len(line), 3)]

    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))

    return ''.join([codon_table[i] for i in data]).replace('*', '')

if __name__ == '__main__':
    print(main())
