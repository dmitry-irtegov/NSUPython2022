def get_bottle_text(count):
    """
    Generates text for the specified number of bottles.

    :param count: The number of bottles
    :return: The generated text
    """

    if not isinstance(count, int) or 0 > count > 10:
        raise ValueError('The count value must be an integer in the range [0, 10].')

    numbers = ('no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    return f'{numbers[count]} green bottle{"s" if count != 1 else ""}'


def generate_song():
    """
    Generates lyrics for the song "Ten Green Bottles".

    :return: The generated lyrics
    """

    hanging = 'hanging on the wall'
    song = []

    for i in range(10, 0, -1):
        line = f'{get_bottle_text(i).capitalize()} {hanging},'
        song.append(line)
        song.append(line)

        line_start = 'And if' if i != 1 else 'If that'
        song.append(f'{line_start} {get_bottle_text(1)} should accidentally fall,')
        song.append(f'There\'ll be {get_bottle_text(i - 1)} {hanging}.')

    return '\n'.join(song)


if __name__ == '__main__':
    print(generate_song())
