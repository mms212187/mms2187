def main():
    # Запросить у пользователя ввод трех чисел
    chislo1 = float(input("Введите первое число: "))
    chislo2 = float(input("Введите второе число: "))
    chislo3 = float(input("Введите третье число: "))

    choice = int(input("Выберите операцию (1 - сумма, 2 - произведение): "))

    if choice == 1:

        result = chislo1 + chislo2 + chislo3
        print("Сумма трех чисел:", result)
    elif choice == 2:

        result = chislo1 * chislo2 * chislo3
        print("Произведение трех чисел:", result)
    else:
        print("Ошибка: Неверный выбор операции")


if __name__ == "__main__":
    main()


def main():

    chislo1 = float(input("Введите первое число: "))
    chislo2 = float(input("Введите второе число: "))
    chislo3 = float(input("Введите третье число: "))

    choice = int(input("Выберите операцию (1 - максимум, 2 - минимум, 3 - среднее): "))

    if choice == 1:

        result = max(chislo1, chislo2, chislo3)
        print("Максимум из трех чисел:", result)
    elif choice == 2:

        result = min(chislo1, chislo2, chislo3)
        print("Минимум из трех чисел:", result)
    elif choice == 3:

        result = (chislo1 + chislo2 + chislo3) / 3
        print("Среднее арифметическое трех чисел:", result)
    else:
        print("Ошибка: Неверный выбор операции")


if __name__ == "__main__":
    main()


def meters_to_miles(meters):
    return meters * 0.000621371


def meters_to_inches(meters):
    return meters * 39.3701


def meters_to_yards(meters):
    return meters * 1.09361


def main():
    # Запрос у пользователя ввод количества метров
    meters = float(input("Введите количество метров: "))

    # Запрос выбор пользователя (1 - мили, 2 - дюймы, 3 - ярды)
    choice = int(input("Выберите единицу измерения (1 - мили, 2 - дюймы, 3 - ярды): "))

    if choice == 1:
        # Перевод метров в мили
        result = meters_to_miles(meters)
        print(f"{meters} метров = {result} миль")
    elif choice == 2:
        # Перевод метров в дюймы
        result = meters_to_inches(meters)
        print(f"{meters} метров = {result} дюймов")
    elif choice == 3:
        # Перевод метров в ярды
        result = meters_to_yards(meters)
        print(f"{meters} метров = {result} ярдов")
    else:
        print("Ошибка: Неверный выбор единицы измерения")


if __name__ == "__main__":
    main()
