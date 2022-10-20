from functools import lru_cache


# https://rosalind.info/problems/fib/

@lru_cache()
def custom_fib(n, k):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    else:
        return custom_fib(n-1, k) + k * custom_fib(n-2, k)


def main():
    with open('data/p004.txt', 'r') as f:
        data = [int(i) for i in f.readline().split()]
    return custom_fib(data[0], data[1])


if __name__ == '__main__':
    print(main())
