
# https://rosalind.info/problems/rna/

def main():
    with open('data/p002.txt', 'r') as f:
        data = f.readline()
    return f"{data.replace('T', 'U')}"


if __name__ == '__main__':
    print(main())
