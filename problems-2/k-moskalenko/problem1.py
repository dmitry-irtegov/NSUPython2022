if __name__ == '__main__':
    n = int(input("Enter the upper bound for Pythagorean triples: "))
    print([
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in range(y, n + 1)
        if x * x + y * y == z * z
    ])
