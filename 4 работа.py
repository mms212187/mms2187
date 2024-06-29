# Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный текст.
def capitalize_reserved_words(text, reserved_words):
    # Разделяем текст на слова
    words = text.split()

    # Проходимся по каждому слову
    for i in range(len(words)):
        # Если слово есть в списке зарезервированных слов, изменяем его регистр на верхний
        if words[i] in reserved_words:
            words[i] = words[i].upper()

    # слитный текст
    modified_text = ' '.join(words)
    return modified_text

# юзер вводит текст
text = input("Введите текст: ")

# Получаем список зарезервированных слов от юзера
reserved_words = input("Введите список зарезервированных слов через пробел: ").split()

# Изменяем регистр зарезервированных слов в тексте и выводим результат
modified_text = capitalize_reserved_words(text, reserved_words)
print("Измененный текст:")
print(modified_text)

# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.

def count_sentences(text):
    # Предполагаем, что предложения разделены точками, восклицательными знаками и вопросительными знаками.

    sentence_delimiters = ['.', '!', '?']
    count = 0
    for char in text:
        if char in sentence_delimiters:
            count += 1
    return count

# Пример текста для тестирования
text = "Это пример текста. В нем есть несколько предложений! Каждое из них отделено знаком пунктуации?"
num_sentences = count_sentences(text)
print("Количество предложений в тексте:", num_sentences)

def censure(text, censured_words):
    new_text = text
    for word in censured_words:
        while word in new_text:
            start_index = new_text.find(word)
            end_index = start_index + len(word)
            first_section = new_text[:start_index]
            second_section = new_text[end_index:]
            new_text = first_section + second_section
    return new_text

# Проблема ,в том что мы перезаписывам переменную new_text на каждой итерации цикла, а не добавляем к ней все секции текста. В результате остаётся только последняя секция, из которой удаляется слово.