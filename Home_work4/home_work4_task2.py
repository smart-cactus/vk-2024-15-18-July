def count(str):
    # Преобразуем строку в нижний регистр и заменяем дефисы пробелами для разделения слов
    str = str.lower().replace('-', ' ')
    
    # Разделяем строку на слова
    words = str.split()
    
    # Создаем словарь для подсчета слов
    word_count = {}
    
    # Подсчитываем каждое слово
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word, count in word_count.items():
        print(f"{word} {count}")

str = input("Введите строку: ")

count(str)
