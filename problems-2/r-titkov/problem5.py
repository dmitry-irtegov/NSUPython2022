import math
import sys


def generate_primes(upper_bound):
	"""
	Generates a list of primes not higher than the upper_bound

	:param upper_bound: maximum prime number
	:return: list of prime numbers
	"""

	if not isinstance(upper_bound, int):
		raise TypeError("Upper bound must be an integer.")

	return [
		num for num in range(2, upper_bound + 1)
		if all(num % divider != 0 for divider in range(2, int(math.sqrt(num)) + 1))
	]


if __name__ == '__main__':
	print('Enter upper bound for prime number generator:', end=' ')
	try:
		upper_bound = int(input())
	except KeyboardInterrupt as e:
		print('KeyboardInterrupt received, exiting...')
		sys.exit()
	except EOFError as e:
		print('EOFError received, exiting...')
		sys.exit()
	except Exception as e:
		sys.exit(f'User input error: {e}')

	try:
		print(generate_primes(upper_bound))
	except TypeError as e:
		sys.exit(e)
