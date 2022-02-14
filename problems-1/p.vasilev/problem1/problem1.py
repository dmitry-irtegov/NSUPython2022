def problem1(num_list: [int]) -> [int]:
    res: [int] = []
    s: int = 0
    for i in num_list:
        res.append(s)
        s += i
    res.append(s)
    return res


if __name__ == '__main__':
    print(problem1([1, 2, 3, 4, 5]))
