def cut(input, upper_limit, lower_limit):
    if upper_limit < lower_limit:
        raise ValueError("upper limit less then lower limit")
    def susbtitute(x):
        if x > upper_limit:
            return upper_limit
        if x < lower_limit:
            return lower_limit
        return x
    return [susbtitute(x) for x in input]

if __name__ == '__main__':
    print("cut([1,2,3,4,5,4,3,2,1], 4, 2) should be [2,2,3,4,4,4,3,2,2]")
    print(cut([1,2,3,4,5,4,3,2,1], 4, 2))
