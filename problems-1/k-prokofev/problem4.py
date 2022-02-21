#!/usr/bin/env python3

def singSong():
    numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']

    start_line = ' green bottle{s} hanging on the wall,'
    middle_line = '{} one green bottle should accidentally fall{}'
    end_line = ' green bottle{} hanging on the wall.'

    for i in range(10):
        print(numbers[i] + start_line.format(s = 's' if i != 9 else ''))
        print(numbers[i] + start_line.format(s = 's' if i != 9 else ''))
        print(middle_line.format('And if' if i != 9 else 'If that', ',' if i != 9 else ''))
        print("There'll be " + numbers[i + 1].lower() + end_line.format('s' if i != 9 else ''))


if __name__ == '__main__':
    singSong()