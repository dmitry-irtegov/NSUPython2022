import sys

def get_pythagorean_triples(limit):
	"""
	Return Pythagorean triples where all numbers are at most limit

	:param limit: maximum value of triplet element
	:return: list of triplets
	"""
	return [
		(m*m - n*n, 2 * m * n, m*m + n*n) 
		for m in range(2, limit)
		for n in range(1, m) 
		if m*m + n*n <= limit
	]

if __name__ == '__main__':
	try:
		number = int(input())
	except (ValueError, TypeError):
		sys.exit('The input must be a single integer')
	except EOFError as e:
		print('EOF received')
		sys.exit()
	except KeyboardInterrupt as e:
		print('KeyboardInterrupt received')
		sys.exit()
	except Exception as e:
		sys.exit(f'Error occured: {e}')

	print(get_pythagorean_triples(number))
