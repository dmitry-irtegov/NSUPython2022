from enum import Enum

fall = "one green bottle should accidentally fall"

green_bottles = ' green bottles hanging on the wall'
comma = ','
dot = '.'
second_string = 'And if ' + fall + comma
third_string_beginning = "There'll be "

pre_last_string = 'If that ' + fall


class Count(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10


def song_printer():
    count = 10
    while count >= 1:
        print(Count(count).name + green_bottles + comma)
        print(Count(count).name + green_bottles + comma)
        if count == 1:
            print(pre_last_string)
            print(third_string_beginning + 'no' + green_bottles + dot)
            break
        else:
            print(second_string)
            count -= 1
            print(third_string_beginning + Count(count).name.lower() + green_bottles + dot)


if __name__ == "__main__":
    song_printer()
