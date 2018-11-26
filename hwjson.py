import json
from collections import Counter


# Открываем и считываем json файл
def open_json_file():
    with open('files\\newsafr.json', encoding='utf-8') as datafile:
        json_data = json.load(datafile)
    return json_data


# Получаем список слов из новостей больше 6 символов
def get_all_long_words():

    string_descriptions = ''

    for items in open_json_file()["rss"]["channel"]["items"]:
        string_descriptions += items["description"]

    list_descriptions = string_descriptions.split()
    long_words = []

    for word in list_descriptions:
        if len(word) > 6:
            long_words.append(word.lower())

    return long_words


# Считаем вхождения слов в списке. Получаем словарь. Через модуль Collections
# def count_long_words():
#
#     long_words = get_all_long_words()
#     count_word_dict = Counter(long_words)
#
#     return count_word_dict
#
#
# # Выводим топ-10 часто встречающихся слов
# def get_top10_words():
#
#     count_word_dict = count_long_words()
#     top10_words = count_word_dict.most_common(10)
#
#     return top10_words
#
#
# if __name__ == "__main__":
#     get_top10_words()

# Считаем вхождения слов в списке. Получаем словарь. Через обычный цикл
def count_long_words():

    count_word_dict = {}

    for long_word in get_all_long_words():
        if long_word in count_word_dict:
            count_word_dict[long_word] += 1
        else:
            count_word_dict[long_word] = 1

    return count_word_dict


# Выводим топ-10 часто встречающихся слов используя .sorted
def get_top10_words():

    count_word_dict = count_long_words()

    def by_value(count_word_dict):
        return count_word_dict[1]

    top10_long_words = sorted(count_long_words().items(), key=by_value, reverse=True)
    print(top10_long_words[0:10])


if __name__ == "__main__":
    get_top10_words()


