
# https://rosalind.info/problems/gc/

def main():
    with open('data/p005.txt', 'r') as f:
        data = [i.removesuffix('\n') for i in f.readlines()]

    for i in range(len(data) - 1, 0, -1):
        if not data[i].startswith('>') and not data[i-1].startswith('>'):
            data[i-1] += data[i]
            del data[i]

    info = { data[i]: data[i+1] for i in range(len(data) - 1)[::2] }

    for key, value in info.items():
        info[key] = (value.count('G') + value.count('C')) / len(value)

    return max(info, key=info.get)[1:], info[max(info, key=info.get)]

if __name__ == '__main__':
    location, prob = main()
    print(f'{location}\n{prob*100}')
