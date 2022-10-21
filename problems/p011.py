from functools import lru_cache


# https://rosalind.info/problems/fibd/

@lru_cache()
def custom_fib(n, m):
    if n < 1:
        return {
            'babies': 0,
            'adults': 0,
        }
    if n == 1:
        return {
            'babies': 1,
            'adults': 0,
        }
    if n == 2:
        return {
            'babies': 0,
            'adults': 1,
        }
    adults = custom_fib(n-1, m)['babies'] + custom_fib(n-1, m)['adults'] - custom_fib(n-m, m)['babies']
    babies = custom_fib(n-1, m)['adults']
    return {
        'babies': babies,
        'adults': adults
    }

def main():
    with open('data/p011.txt', 'r') as f:
        data = [int(i) for i in f.readline().split()]
    return custom_fib(data[0], data[1])


if __name__ == '__main__':
    print(sum(main().values()))
