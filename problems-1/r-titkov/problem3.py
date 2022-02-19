def test_hypothesis(number):
	"""
	The function tests the Collatz hypothesis for a given number and outputs a chain of transformations
	"""
	if number <= 0:
		raise ValueError("The value must be positive integer")

	while number != 1:
		print(number, end=' ')
		if number % 2 == 0:
			number //= 2
		else:
			number = 3 * number + 1
		print('->', end=' ')

	print(number)
	return True

if __name__ == '__main__':
	print('Enter the number: ', end='')
	number = int(input())
	if test_hypothesis(number):
		print('Hypothesis is correct')
	else:
		print('Hypothesis is incorrect')
