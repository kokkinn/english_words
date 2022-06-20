import json
import random
import sqlite3

file = open("words.json", "r")


def create_dict(json_file):
    return json.load(json_file)


def test_rus_eng(dict_words):
    list_of_tupples = list(dict_words.items())
    while True:
        intt = random.randint(1, len(list_of_tupples) - 1)
        tuplee = list_of_tupples[intt]
        print(f"Enter a translation for '{tuplee[1]}'...")
        ans = input()
        if ans == tuplee[0]:
            print("Success")
            list_of_tupples.remove(list_of_tupples[intt])
        else:
            print(f"Incorrect, correct answer is '{tuplee[0]}'")


def enter_new_words():
    filee = open("words.json", "w")
    temp_dict = {}
    while True:
        flag_exit = False
        while True:
            word_in_english = input("Please enter a word in English")
            if not word_in_english:
                print("Error")
            elif word_in_english == "0":
                flag_exit = True
                break
            else:
                break
        while True:
            word_in_russian = input("Please enter a translation for this word")
            if not word_in_russian:
                print("Error")
            else:
                break
        temp_dict[word_in_english] = word_in_russian
        if flag_exit:
            break
    filee.write(json.dumps(temp_dict, ensure_ascii=False))

# a = create_dict(file)
# test_rus_eng(a)
# print(a.items())

enter_new_words()
