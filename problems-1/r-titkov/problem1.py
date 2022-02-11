def cumSum(input):
	sum_list = [0]
	for num in input:
		new_sum = sum_list[-1] + num
		sum_list.append(new_sum)

	return sum_list

if __name__ == "__main__":
	print(f'cumSum([1,2,3]) == [0, 1, 3, 6] is {cumSum([1,2,3]) == [0, 1, 3, 6]}')