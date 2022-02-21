def collatz(num):
    """
    Tests if the Collatz hypothesis holds for the specified number.

    :param num: The specified number
    :return: The chain of transformations
    """

    if num <= 0:
        raise ValueError('The input number must be a positive integer.')

    chain = [num]

    while chain[-1] != 1:
        if chain[-1] % 2 == 0:
            chain.append(chain[-1] // 2)
        else:
            chain.append(3 * chain[-1] + 1)

    return chain


if __name__ == '__main__':
    number = int(input('Enter a natural number: '))
    result = ' -> '.join(map(str, collatz(number)))
    print('Result:', result)
