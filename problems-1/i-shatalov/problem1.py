def cumulative(array):
    res = 0
    tmpArr = [0]
    for x in array:
        res += x
        tmpArr.append(res)
    return tmpArr


if __name__ == "__main__":
    try:
        input_array = [int(value) for value in input("Please enter array of numbers: ").split()]
        print(cumulative(input_array))
    except ValueError as e:
        print("Error: ", e)
    except BaseException:
        print("Error! Please enter array of integer numbers separated with space.")
