def cum_sum(input):
    res = [0]
    for x in input:
        last = res[-1]
        res.append(x + last)
    return res

if __name__ == '__main__':
    print(f"cum_sum [1,2,3,4,5] should be [0, 1, 3, 6, 10, 15] : {cum_sum([1,2,3,4,5])}")

