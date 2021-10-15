def collatz(n: int, i: int = 0, verbose: bool = False) -> int:
    """
    This function returns the number of iterations of 
    the Collatz sequence until reaching 1 starting from n.
    """
    i = 0
    if verbose:
        print(n)
    if n != 1:
        n = n // 2 if n % 2 == 0 else (n * 3) + 1
        return collatz(n, i, verbose)
    else:
        return i


def collatz_sequence(n: int,
                     sequence: list[int] = [],
                     verbose: bool = False) -> list[int]:
    """
    This function returns the Collatz sequence starting from n.
    """
    sequence.append(n)
    if verbose:
        print(n)
    if n != 1:
        n = n // 2 if n % 2 == 0 else (n * 3) + 1
        return collatz_sequence(n, sequence, verbose)
    else:
        return sequence


def get_valid_positive_int() -> None:
    while True:
        try:
            return int(input('Please, enter a positive integer: '))
        except:
            print('The input value is not a positive integer.\n')
            get_valid_positive_int()


def print_int_list_tabs(l: list[int]) -> None:
    max_len = len(str(max(l))) + 1
    buffer = ''
    for e in l:
        buffer += ('{:<' + str(max_len) + '}\t').format(e)
    print(buffer)


if __name__ == '__main__':
    while True:
        user_input = input('Get Collatz sequence (s) or ' +
                           'the number of iterations(i): ')
        if user_input in ['q', 'exit', '0']:
            break
        elif user_input == 'i':
            collatz(get_valid_positive_int(), verbose=True)
        elif user_input == 's':
            print_int_list_tabs(collatz_sequence(get_valid_positive_int()))
        else:
            print('Please, enter a valid option. ' +
                  'Either s or i.')
