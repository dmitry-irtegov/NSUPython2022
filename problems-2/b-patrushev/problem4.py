#!/usr/bin/env python3
"""
This module implements solution for problem 4 in Problems-2 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-2.pdf
"""

if __name__ == '__main__':
    print('Enter sequence to search for:')
    seq = input()
    match = []
    match_cnt = 0

    with open('pi.txt', 'r') as pi:
        digits = ''.join(pi.read()[2:].split('\n'))

    cur_pos = digits.find(seq, 0)
    while cur_pos != -1:
        if match_cnt < 5:
            match.append(cur_pos)
        match_cnt += 1
        cur_pos += 1
        cur_pos = digits.find(seq, cur_pos)

    print(f'Found {match_cnt} results.')
    print(f'Positions: {" ".join(map(str, match))} ...')
