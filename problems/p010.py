
# https://rosalind.info/problems/cons/

def main():
    with open('data/p010.txt', 'r') as f:
        data = [i for i in f.read().split('\n')]

    for i in range(len(data) - 1, 0, -1):
        if not data[i].startswith('>') and not data[i-1].startswith('>'):
            data[i-1] += data[i]
            del data[i]

    data = data[1::2]

    length = len(data[0])

    amount = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length,
    }

    for i in data:
        for count, char in enumerate(i):
            amount[char][count] += 1

    consensus = ''.join([max(amount, key=lambda x : amount.get(x)[i]) for i in range(length)])
    profile = '\n'.join([f'{key}: {" ".join([str(i) for i in value])}' for key, value in amount.items()])
    return f'{consensus}\n{profile}'



if __name__ == '__main__':
    print(main())
