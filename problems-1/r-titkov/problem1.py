def cumSum(array):
	sum_list = [0]
	for num in array:
		new_sum = sum_list[-1] + num
		sum_list.append(new_sum)

	return sum_list

if __name__ == "__main__":
	print('Enter integers:', end=' ')
	array = list(map(int, input().split()))
	print(f'Result: {cumSum(array)}')