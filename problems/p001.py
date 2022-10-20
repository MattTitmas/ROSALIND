
# https://rosalind.info/problems/dna/

def main():
    with open('data/p001.txt' , 'r') as f:
        data = f.readline()
    return f"{data.count('A')} {data.count('C')} {data.count('G')} {data.count('T')}"


if __name__ == '__main__':
    print(main())
