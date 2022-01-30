import sys


def naive_primes(n: int) -> list[int]:
    """Return all the prime numbers up to n"""
    assert n > 2
    primes_list = [2]
    for i in range(3, n + 1):
        if naive_is_prime(i, primes_list):
            primes_list.append(i)
    return primes_list


def naive_primes_recursive(i: int, m: int, l: list[int]) -> list[int]:
    """Return all the prime numbers up to m.
    """
    assert m >= i
    if naive_is_prime(i, l):
        l.append(i)
    return l if i == m else naive_primes_recursive(i + 1, m, l)


def naive_is_prime(n: int, l: list[int]) -> bool:
    for prime in l:
        if n % prime == 0:
            return False
    return True


if __name__ == '__main__':
    print(sys.getrecursionlimit())
    user_input = int(input('Insert integer limit to primes list: '))
    while user_input > 2:
        sys.setrecursionlimit(user_input + 1)
        print(naive_primes_recursive(3, user_input, [2]))
        user_input = int(input('Insert integer limit to primes list: '))
