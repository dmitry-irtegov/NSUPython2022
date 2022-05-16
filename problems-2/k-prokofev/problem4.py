import sys


def find_substrings():
    file_path = input("Filepath: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as source:
            seq = input("Enter sequence to search for: ")
            text = ''.join(source.read()[2:].split('\n'))
    except OSError as e:
        sys.exit(f'{e.filename}: {e.strerror}')
    return finder(seq, text)


def finder(seq, text):
    i = 0
    counter = 0
    positions = []
    while True:
        i = text.find(seq, i + 1)
        if i == -1:
            break
        counter += 1
        if counter < 6:
            positions.append(i)
    return counter, positions

if __name__ == '__main__':
    count, positions = find_substrings()
print("Found " + str(count) + " results.")
print("Positions: " + str(positions))
