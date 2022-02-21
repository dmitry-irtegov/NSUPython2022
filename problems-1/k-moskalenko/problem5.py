def get_primes(num):
    """
    Returns the prime factors of a number.

    :param num: The number to factorize
    :return: The list of prime factors
    """

    i = 2
    factors = {}

    while i * i <= num:
        if num % i != 0:
            i += 1
        else:
            num //= i
            factors[i] = factors.get(i, 0) + 1

    if num > 1:
        factors[num] = factors.get(num, 0) + 1

    result = []
    for key in sorted(factors.keys()):
        result.append([key, factors[key]])

    return result


if __name__ == '__main__':
    number = int(input('Enter a number to factorize: '))
    print('Result:', get_primes(number))
