import math

# solution
def primesTilX(x):
    return [x for x in range(2, x) if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))]

if __name__ == '__main__':
    print(f"primesTilX(10) == f{primesTilX(10)}")
