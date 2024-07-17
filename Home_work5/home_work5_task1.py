def cutString(arr):
    result = []
    # Проходим по каждому слову в списке
    for word in arr:

        if len(word) > 10:
            # Обрезаем слово до 7 символов и добавляем '...'
            new_word = word[:7] + '...'
        else:
            # Если длина слова 10 или меньше, оставляем его без изменений
            new_word = word
        # Добавляем обработанное слово в результирующий список
        result.append(new_word)
    
    # Выводим список слов после обработки
    print(result)

# Пример использования функции
words = list(map(str, input().split()))
cutString(words)
