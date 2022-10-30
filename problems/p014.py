from useful_classes import ReadFasta, Substrings


# https://rosalind.info/problems/lcsm/

def main():
    fasta_reader = ReadFasta('data/p014.txt')

    sequences = fasta_reader.get_list()

    substrings = Substrings(sequences[0], sequences[1]).all_substring()
    for substring in substrings[::-1]:
        for i in sequences[2:]:
            if not substring in i:
                continue
        return substring
    return ""



if __name__ == '__main__':
    print(main())
