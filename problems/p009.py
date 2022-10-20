import re

# https://rosalind.info/problems/subs/

def main():
    with open('data/p009.txt', 'r') as f:
        data = f.read().split('\n')

    return ' '.join([str(m.start() + 1) for m in re.finditer(f'(?={data[1]})', data[0])])



if __name__ == '__main__':
    print(main())
