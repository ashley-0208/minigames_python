from random import choice


def select_word():
    with open('word.txt', mode='r', encoding='utf-8') as words:
        word_list = words.readlines()
    return choice(word_list).strip().upper()


print(select_word())


