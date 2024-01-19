from primes.prime_tools import is_prime


def is_perfect_number(n: int) -> bool:
    if n < 2:
        return False
    sum = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False


def generate_perfect_number_euclid(k: int) -> int:
    if is_prime(k):
        return 2**(k-1)*(2**k-1)
    else:
        raise ValueError('k must be prime')
    return 0


if __name__ == '__main__':
    print(is_perfect_number(6))
    print(generate_perfect_number_euclid(4))
    print(generate_perfect_number_euclid(5))
