import random

def guess_number():
    # Генерируем случайное число от 1 до 100
    target = random.randint(1, 100)
    
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = int(input("Введите ваше число: "))

        # Сравниваем введенное число с загаданным числом
        if guess < target:
            print("Число больше!")
        elif guess > target:
            print("Число меньше!")
        else:
            print("Ты угадал!")
            break

guess_number()
