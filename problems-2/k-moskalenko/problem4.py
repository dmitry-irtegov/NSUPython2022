import sys


def find_all(string, sub):
    """
    Finds all indices of the substring in the string.

    :param string: the specified string
    :param sub: the specified substring
    :return: the list of indices
    """

    start = 0
    result = []

    while True:
        start = string.find(sub, start)
        if start == -1:
            return result
        result.append(start)
        start += 1


def get_input():
    """
    Reads the user input and validates it is an integer.

    :return: the stripped user input
    """

    print('Enter sequence to search for.')
    input_str = input('> ').strip()

    if not input_str.isdigit():
        raise ValueError('The input must be an integer.')

    return input_str


if __name__ == '__main__':
    try:
        with open('pi.txt', 'r') as file:
            lines = map(str.strip, file)
            pi = ''.join(lines)[2:]
    except OSError as e:
        sys.exit(f'{e.filename}: {e.strerror}')

    while True:
        try:
            substr = get_input()
        except Exception as e:
            print(f'User input failed: {e}\n', file=sys.stderr)
            continue

        indices = find_all(pi, substr)
        positions = ' '.join(map(str, indices[:5]))

        if len(indices) > 0:
            print(f'Found {len(indices)} results.')
            print(f'Positions: {positions} {"..." if len(indices) > 5 else ""}')
        else:
            print('Nothing found.')
        print()
