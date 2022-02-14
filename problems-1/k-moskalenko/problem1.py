def cum_sum(nums):
	result = [0]
	for num in nums:
		result.append(result[-1] + num)
	return result


if __name__ == '__main__':
	in_str = input('Enter the numbers to sum: ')
	result = cum_sum(map(int, in_str.split()))
	print('Result:', result)
