
# https://rosalind.info/problems/grph/

def main():
    with open('data/p012.txt', 'r') as f:
        data = [i for i in f.read().split('\n')]

    for i in range(len(data) - 1, 0, -1):
        if not data[i].startswith('>') and not data[i-1].startswith('>'):
            data[i-1] += data[i]
            del data[i]
        elif data[i].startswith('>'):
            data[i] = data[i][1:]
    data[0] = data[0][1:]

    data = {i: data[count*2 + 1] for count, i in enumerate(data[::2])}

    to_return = [[(key, key_inner) for key_inner, value_inner in data.items()
                 if (key != key_inner and value[-3:] == value_inner[:3])]
                 for key, value in data.items()]

    return '\n'.join([' '.join([a, b]) for sublist in to_return for (a, b) in sublist])


if __name__ == '__main__':
    print(main())
