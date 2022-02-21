def create_dict(filename):
    """
    Reads the file and constructs a reversed dictionary.

    :param filename: The specified filename
    :return: The constructed dictionary
    """

    result = {}
    with open(filename, 'r') as f:
        for line in f:
            english, latin = map(str.strip, line.split('-'))
            for word in map(str.strip, latin.split(',')):
                if word not in result:
                    result[word] = set()
                result[word].add(english)
    return result


if __name__ == '__main__':
    dictionary = create_dict('dict.txt')
    for key in sorted(dictionary.keys()):
        translations = sorted(dictionary[key])
        print(key, '-', ', '.join(translations))
