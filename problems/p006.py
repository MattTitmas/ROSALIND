
# https://rosalind.info/problems/hamm/

def main():
    with open('data/p006.txt', 'r') as f:
        data = [list(i.removesuffix('\n')) for i in f.readlines()]


    return sum([1 if x != y else 0 for (x, y) in zip(data[0], data[1])])

if __name__ == '__main__':
    print(main())
