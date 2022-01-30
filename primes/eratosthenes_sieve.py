def eratosthenes_sieve(n: int) -> list[int]:
    numbers = list(range(2, n+1))
    primes = list(range(2, n+1))
    length = n-1
    eratosthenes_sieve_r(0, primes, numbers, length, length)
    return primes


def eratosthenes_sieve_r(i: int,
                         primes: list[int],
                         original: list[int], 
                         ori_len: int,
                         length: int) -> list[int]:
    if i == length:
        return primes
    current = primes[i]
    maximum = ori_len//current
    if maximum > i:
        for e in original[i:maximum]:
            composite = e*current
            if composite in primes:
                primes.remove(composite)
                length -= 1
    print('i: ' + str(i) + '\t' + str(primes))
    return eratosthenes_sieve_r(i + 1, primes, original, ori_len, length)


if __name__ == '__main__':
    print(eratosthenes_sieve(1000))
