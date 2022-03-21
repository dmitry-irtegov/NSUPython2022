import sys

def factorize(number):
	"""
	The function takes an integer to factorize and
	returns the factorization for the given number

	:param number: The number to factorize
	:type number: int
	:return: The factorization for the given number
	"""

	if not isinstance(number, int):
		raise ValueError("Number must be an integer")

	if number < 1:
		raise ValueError("Number must be greater than zero")

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

	try:
		print(factorize(number))
	except Exception as e:
		sys.exit(f"Error occured: {e}")
