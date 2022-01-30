def eratosthenes_sieve(n: int) -> list[int]:
    numbers = list(range(2, n+1))
    # for e in numbers[0:(numbers[-1]//numbers[0]-1)]:
    #     numbers.remove(e*numbers[0])
    eratosthenes_sieve_r(0, numbers, n-1)
    return numbers


def eratosthenes_sieve_r(i: int, l: list[int], length: int) -> list[int]:
    if i == length:
        return l
    current = l[i]
    maximum = (length//current)
    if maximum > i:
        for e in l[i:maximum]:
            composite = e*current
            l.remove(e*current)
            length -= 1
    print(l)
    return eratosthenes_sieve_r(i + 1, l, length)


if __name__ == '__main__':
    print(eratosthenes_sieve(100))
