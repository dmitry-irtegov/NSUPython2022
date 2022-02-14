#!/usr/bin/env python3

def cum_sum(nums):
    res = [0]
    total = 0
    for num in nums:
        total += num
        res.append(total)
    return res


if __name__ == '__main__':
    inp = list(map(int, input().split()))
    print(cum_sum(inp))
