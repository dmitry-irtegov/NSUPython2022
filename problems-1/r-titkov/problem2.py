def numberCutter(nums, a, b):
	if a > b:
		raise ValueError('The lower limit must be less than the upper limit')

	for i in range(len(nums)):
		if nums[i] < a:
			nums[i] = a
		elif nums[i] > b:
			nums[i] = b

if __name__ == '__main__':
	print('Enter array of numbers:', end=' ')
	array = list(map(int, input().split()))
	print('Enter lower and upper bound:', end=' ')
	a, b = map(int, input().split())
	numberCutter(array, a, b)
	print(f'Result: {array}')
