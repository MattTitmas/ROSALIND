
# https://rosalind.info/problems/revc/

def main():
    compliments = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    with open('data/p003.txt', 'r') as f:
        data = f.readline()[:-1]
    return ''.join([compliments[i] for i in data][::-1])


if __name__ == '__main__':
    print(main())
