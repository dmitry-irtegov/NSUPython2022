import sys

def factorize(number):
	"""
	The function takes a number to factorize and
	returns the factorization for the given number

	:param number: The number to factorize
	:return: The factorization for the given number
	"""

	if number == 1:
		return [[1, 1]]

	factorization = []
	for divider in range(2, number + 1):
		degree = 0

		while (number % divider) == 0:
			number //= divider
			degree += 1

		if degree > 0:
			factorization.append([divider, degree])
		
		if number == 1:
			break

	return factorization


if __name__ == '__main__':
	print("Enter a number to factorize: ", end='')

	try:
		number = int(input())
	except KeyboardInterrupt:
		print("\nKeyboardInterrupt received")
		sys.exit()
	except EOFError:
		print("\nEOFError received")
		sys.exit()
	except Exception as e:
		sys.exit(f"Error occured: {e}")

	if number < 1:
		sys.exit("Number must be greater than zero")

	print(factorize(number))
