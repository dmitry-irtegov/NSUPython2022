import sys
from argparse import ArgumentParser


def tr(string, to_replace='', replace='', delete=''):
    if len(to_replace) != len(replace):
        raise ValueError('Incorrect translate table: lengths of translate table rows is not equal.')
    test_set = set()
    for c in to_replace:
        if c in test_set:
            raise ValueError('List of replaceable characters contains duplicates.')
        test_set.add(c)
    res = string
    for c in delete:
        res = res.replace(c, '')
    for i in range(0, len(to_replace)):
        res = res.replace(to_replace[i], replace[i])

    return res


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('filepath', nargs='?', help="Path to file with text.", default='')
    parser.add_argument('toreplace', nargs='?', help="Characters.", default='')
    parser.add_argument('replace', nargs='?', help="Replacement.", default='')
    parser.add_argument("-d", "--delete", dest="delete", default='', const='', nargs='?',
                        help="Characters to delete.")
    options = parser.parse_args()
    try:
        with open(options.filepath, 'r') as file:
            s = file.read(1000)
            if s == '':
                exit()
            try:
                print(tr(s, options.toreplace, options.replace, options.delete), end='')
            except Exception as e:
                print('Error while calling "tr()":\n' + str(e), file=sys.stderr)
                exit(1)
    except Exception as e:
        print('Error while calling "open()":\n' + str(e), file=sys.stderr)
        exit(1)
