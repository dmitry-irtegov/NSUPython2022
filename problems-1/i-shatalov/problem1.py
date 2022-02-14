def cumalative(array):
    sum = 0
    tmpArr = [0]
    for x in array:
        sum += x
        tmpArr.append(sum)
    return tmpArr


if __name__ == "__main__":
    print(cumalative([1, 2, 3, 4]))