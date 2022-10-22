
# https://rosalind.info/problems/iev/

def main():
    with open('data/p013.txt', 'r') as f:
        data = [int(i.strip('\n')) for i in f.read().split(' ')]
    order = [2, 2, 2, 3/2, 1, 0]
    return sum([a * b for a, b in zip(data, order)])


if __name__ == '__main__':
    print(main())
