import re

def getReverseDictByFileName(filename):

    orig_dict = {}
    with  open(filename, 'r') as orig_dict_file:
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
    new_dict = getReverseDictByFileName('dict.txt')
    print("Result is: ")
    for key in sorted(new_dict.keys()):
        translations = new_dict[key]
        print(f"{key} - {', '.join(translations)}")
    

