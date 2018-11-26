import xml.etree.ElementTree as ET


# Читаем xml файл, добираемся до discription
def open_xml_file():
    parser = ET.XMLParser(encoding = 'utf-8')
    tree = ET.parse('files\\newsafr.xml', parser)
    root = tree.getroot()
    xml_descriptions = root.findall('channel/item/description')
    return xml_descriptions


# Получаем список слов из новостей больше 6 символов
def get_all_long_words():

    string_descriptions = ''

    for description in open_xml_file():
        string_descriptions += description.text

    list_descriptions = string_descriptions.split()
    long_words = []

    for word in list_descriptions:
        if len(word) > 6:
            long_words.append(word.lower())

    return long_words


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

