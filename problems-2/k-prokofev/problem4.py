import sys
import unittest
import argparse

def load_file(filename):
    try:
        with open(filename) as file:
            file.read(2)
            pi_number = file.read().replace('\n', '')
    except OSError as e:
        sys.exit(f'{e.filename}: {e.strerror}')
    return pi_number

def find_substrings(sequence, filename):
    pi = load_file(filename)
    return finder(sequence, pi)

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
    filename = "pi.txt"

    parser = argparse.ArgumentParser(description='Pi sequences finder.')
    parser.add_argument('-f')
    args = parser.parse_args()

    if args.f:
        filename = args.f

    sequence = input("Enter sequence to search for: ")
    count, positions = find_substrings(sequence, filename)
    print("Found " + str(count) + " results.")
    print("Positions: " + str(positions))

