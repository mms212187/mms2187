import random


def display_grades(grades):
    print("Оценки студента:", grades)


def retake_exam(grades):
    try:
        index = int(input("Введите номер оценки для пересдачи (0-9): "))
        if index < 0 or index >= len(grades):
            print("Неверный номер. Попробуйте снова.")
            return
        new_grade = int(input("Введите новую оценку (1-12): "))
        if new_grade < 1 or new_grade > 12:
            print("Неверная оценка. Попробуйте снова.")
            return
        grades[index] = new_grade
    except ValueError:
        print("Неверный ввод. Попробуйте снова.")


def check_scholarship(grades):
    average = sum(grades) / len(grades)
    print(f"Средний балл: {average:.2f}")
    if average >= 10.7:
        print("Стипендия выходит.")
    else:
        print("Стипендия не выходит.")


def sort_grades(grades):
    try:
        order = int(
            input(
                "Введите 1 для сортировки по возрастанию или 2 для сортировки по убыванию: "
            )
        )
        if order == 1:
            grades.sort()
        elif order == 2:
            grades.sort(reverse=True)
        else:
            print("Неверный ввод. Попробуйте снова.")
    except ValueError:
        print("Неверный ввод. Попробуйте снова.")


def main():
    # Фиксированный массив из 10 различных оценок от 1 до 12
    grades = random.sample(range(1, 13), 10)

    while True:
        print("\nМеню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            display_grades(grades)
        elif choice == "2":
            retake_exam(grades)
        elif choice == "3":
            check_scholarship(grades)
        elif choice == "4":
            sort_grades(grades)
            display_grades(grades)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
