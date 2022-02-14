#!/usr/bin/env python3

# NOTE: this solution includes the number 3 before the point
# This will lead to this solution being "off" exactly by 1 (if input is something like 3141, 0 is included)
# i.e. input of "1415" will print "1 6955 ..." instead of "0 6954 ..." , etc
if __name__ == '__main__':
    # pi.txt has to be in the same directory
    with open('pi.txt') as file:
        pi = file.read(-1)

    pi = pi.replace('\n', '')
    pi = pi.replace('.', '')

    print('Enter sequence to search for.')
    inp = input()

    res = []
    t = 0
    while inp in pi[t:]:
        t = pi.find(inp, t)
        res.append(t)
        t += 1
    
    print(f'Found {len(res)} results.')
    print(f'Positions:', *res[:5], '...' if len(res) > 5 else '')
