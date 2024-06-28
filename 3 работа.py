# Пользователь вводит с клавиатуры два числа.
# Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
# а также среднеарифметическое каждой группы. на Python
def calculate_statistics(start, end):
    even_sum = 0
    odd_sum = 0
    multiple_of_9_sum = 0

    even_count = 0
    odd_count = 0
    multiple_of_9_count = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_sum += num
            odd_count += 1

        if num % 9 == 0:
            multiple_of_9_sum += num
            multiple_of_9_count += 1

    even_average = even_sum / even_count if even_count != 0 else 0
    odd_average = odd_sum / odd_count if odd_count != 0 else 0
    multiple_of_9_average = (
        multiple_of_9_sum / multiple_of_9_count if multiple_of_9_count != 0 else 0
    )

    return {
        "even_sum": even_sum,
        "even_average": even_average,
        "odd_sum": odd_sum,
        "odd_average": odd_average,
        "multiple_of_9_sum": multiple_of_9_sum,
        "multiple_of_9_average": multiple_of_9_average,
    }


start_num = int(input("Введите начальное число: "))
end_num = int(input("Введите конечное число: "))

statistics = calculate_statistics(start_num, end_num)
print("Сумма четных чисел:", statistics["even_sum"])
print("Среднее арифметическое чет. чисел:", statistics["even_average"])
print("Сумма нечетных чисел:", statistics["odd_sum"])
print("Среднее арифметическое неч. чисел:", statistics["odd_average"])
print("Сумма чисел, кратных 9:", statistics["multiple_of_9_sum"])
print("Среднее арифметическое чисел кратных 9:", statistics["multiple_of_9_average"])

# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6
# и вывести обратно на экран. Будет плюсом если вы используете управляющие операторы
# continue, break и else.


def remove_digits(num):
    result = ""
    for chislo in str(num):
        if chislo in ["3", "6"]:
            continue  # Пропускаем цифры 3 и 6
        result += chislo
    else:
        if not result:
            print("Результат удаления всех цифр 3 и 6 из числа равен 0.")
        else:
            print("Число после удаления цифр 3 и 6:", result)


user_input = input("Введите любое целое число: ")

try:
    user_number = int(user_input)
    remove_digits(user_number)
except ValueError:
    print("Ошибка: Введите целое число.")
