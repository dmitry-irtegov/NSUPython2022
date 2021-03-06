import re
import sys

def getReverseDictByFileName(filename):

    orig_dict = {}
    try:
        orig_dict_file = open(filename, 'r')
    except IOError as e:
        raise IOError("Can't read dict file") from e
    else:
        with orig_dict_file:
            for line in orig_dict_file:
                words = re.split(', | - ', str.rstrip(line))
                orig = words[0]
                translations = words[1:]
                orig_dict[orig] = translations

    new_dict = {}

    for word, translations in orig_dict.items():
        for translation in translations:
            if not translation in new_dict:
                new_dict[translation] = []
            new_dict[translation].append(word)

    return new_dict




if __name__ == '__main__':
    try:
        new_dict = getReverseDictByFileName('dict.txt')
    except Exception as e:
        cause = e.__cause__
        cause_message = f"because {cause}" if cause is not None else ""
        print(f"Error happened: {e} {cause_message} \n exiting now...", file=sys.stderr)
        exit(1)
    print("Result is: ")
    for key in sorted(new_dict.keys()):
        translations = new_dict[key]
        print(f"{key} - {', '.join(translations)}")
