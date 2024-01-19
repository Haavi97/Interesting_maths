from primes.primeTools import isPrime


def isPerfectNumber(n: int) -> bool:
    if n < 2:
        return False
    sum = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False


def generatePerfectNumberEuclid(k: int) -> int:
    if isPrime(k):
        return 2**(k-1)*(2**k-1)
    else:
        raise ValueError('k must be prime')
    return 0


if __name__ == '__main__':
    print(isPerfectNumber(6))
    print(generatePerfectNumberEuclid(4))
    print(generatePerfectNumberEuclid(5))
