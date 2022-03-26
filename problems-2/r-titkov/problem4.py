import sys


def load_pi_number(filename):
	"""
	The function load pi.txt file and return it's content

	:return: pi.txt file content
	"""
	with open(filename) as file:
		file.read(2)
		pi_number = file.read().replace('\n', '')

	return pi_number


def find_sequences(pi_number, sequence):
	"""
	The function find all occurrences of "sequence" in "pi_number" string
	and return all occurences and occurences count

	:param pi_number: string content where the search will be performed
	:param sequence: int or string which will be searhed in the pi_number
	:return sequences: indexes of all occurrences
	:return sequences_count: count of occurrences
	"""
	if not type(pi_number) is str:
		raise ValueError("Content input error: The 'pi_number' parameter must be a string")

	if isinstance(sequence, int):
		sequence = str(sequence)
	elif not isinstance(sequence, str) or not sequence.isdigit():
		raise ValueError("User input error: The input must be a string sequence of digits")

	sequences_count = 0
	sequences = []
	current_position = pi_number.find(sequence, 0)
	while current_position != -1:
		if sequences_count < 5:
			sequences.append(str(current_position))

		sequences_count += 1
		current_position = pi_number.find(sequence, current_position + 1)

	return sequences, sequences_count


if __name__ == '__main__':
	try:
		pi_number = load_pi_number("pi.txt")
	except OSError as e:
		sys.exit(f'While loading {e.filename} file {type(e)} occurred: {e.strerror}')

	while True:
		print("\nEnter sequence to search for.")
		print('< ', end='')
		try:
			sequence = input()
		except EOFError:
			print('EOFError received, exiting...')
			sys.exit()
		except KeyboardInterrupt:
			print('KeyboardInterrupt received, exiting...')
			sys.exit()
		except OSError as e:
			print(f'{type(e)} occured while reading user input: {e.strerror}')
			continue

		try:
			sequences, sequences_count = find_sequences(pi_number, sequence)
		except Exception as e:
			print(e)
			continue

		print(f'Found {sequences_count} result{"s" if sequences_count > 1 else ""}.')
		if sequences_count > 0:
			print(f'Positions: {" ".join(sequences)} {"..." if sequences_count > 5 else ""}')
		else:
			print('Nothing found')
