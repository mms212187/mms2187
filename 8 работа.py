def get_discount(age):
    match age:
        case age if age < 3:
            return 10
        case age if 3 <= age < 6:
            return 20
        case age if 6 <= age < 10:
            return 30
        case age if 10 <= age < 14:
            return 40
        case age if age >= 14:
            return 50
        case _:
            return 0


def main():
    customers = [
        {"name": "Анна", "age": 2},
        {"name": "Борис", "age": 4},
        {"name": "Виктория", "age": 7},
        {"name": "Георгий", "age": 12},
        {"name": "Дмитрий", "age": 15},
    ]

    for customer in customers:
        age = customer["age"]
        discount = get_discount(age)
        print(
            f"Покупатель {customer['name']} ({age} лет) получает скидку {discount}% на игрушки."
        )


if __name__ == "__main__":
    main()


def get_discount(age):
    match age:
        case age if age < 3:
            return 10
        case age if 3 <= age < 6:
            return 20
        case age if 6 <= age < 10:
            return 30
        case age if 10 <= age < 14:
            return 40
        case age if age >= 14:
            return 50
        case _:
            return 0


def main():
    name = input("Введите имя: ")
    while True:
        try:
            age = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    discount = get_discount(age)
    print(f"Покупатель {name} ({age} лет) получает скидку {discount}% на игрушки.")


if __name__ == "__main__":
    main()


def get_category(total_score):
    match total_score:
        case score if score < 50:
            return "Новичок"
        case score if 50 <= score < 100:
            return "Любитель"
        case score if 100 <= score < 150:
            return "Профессионал"
        case score if score >= 150:
            return "Мастер"
        case _:
            return "Без категории"


def get_scores():
    scores = []
    for i in range(5):
        while True:
            try:
                score = int(input(f"Введите количество очков за бросок {i+1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Пожалуйста, введите корректное число.")
    return scores


def main():
    name = input("Введите имя игрока: ")
    print("Введите количество очков за 5 бросков:")
    scores = get_scores()
    total_score = sum(scores)
    category = get_category(total_score)
    print(
        f"Игрок {name} набрал {total_score} очков и попадает в категорию '{category}'."
    )


if __name__ == "__main__":
    main()
