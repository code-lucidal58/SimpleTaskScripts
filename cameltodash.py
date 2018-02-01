import sys


def camel_to_dash(file_path):
    file_object = open(file_path, 'r+')
    data = file_object.read()
    data_split = data.split()
    dict_new_word = dict()
    for word in data_split:
        if not word[0].isupper():
            new_word = word
            for letter in word:
                if letter.isupper():
                    r = str("_") + chr(ord(letter) - 65 + 97)
                    new_word = new_word.replace(letter, r)
                    print(new_word)
            dict_new_word[word] = new_word
    print(dict_new_word)
    for key in dict_new_word:
        data = data.replace(key, dict_new_word[key])
    print(data)
    file_object.seek(0)
    file_object.write(data)
    file_object.truncate()
    file_object.close()


if __name__ == '__main__':
    file_path = sys.argv[1]
    camel_to_dash(file_path)
