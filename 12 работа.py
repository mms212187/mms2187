from typing import Dict, Tuple, List, Optional


def pick_resistors(resistance: int) -> Optional[Dict[str, Tuple[int, ...]]]:
    """
    Подбирает ближайшие номиналы сопротивлений из каждого ряда сопротивлений.

    Параметры:
    resistance (int): Значение сопротивления в диапазоне от 100 до 999 включительно.
    Возвращает:
    Optional[Dict[str, Tuple[int, ...]]]: Словарь, где ключи - ряды сопротивлений ('E6', 'E12', 'E24', 'E48', 'E96'),
     а значения - кортежи ближайших номиналов сопротивлений.
    Возвращает None, если переданное сопротивление не в диапазоне.
    """
    if not (100 <= resistance <= 999):
        return None

    # Ряды номиналов сопротивлений
    resistor_series: Dict[str, List[int]] = {
        "E6": [100, 150, 220, 330, 470, 680],
        "E12": [100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820],
        "E24": [
            100,
            110,
            120,
            130,
            150,
            160,
            180,
            200,
            220,
            240,
            270,
            300,
            330,
            360,
            390,
            430,
            470,
            510,
            560,
            620,
            680,
            750,
            820,
            910,
        ],
        "E48": [
            100,
            105,
            110,
            115,
            121,
            127,
            133,
            140,
            147,
            154,
            162,
            169,
            178,
            187,
            196,
            205,
            215,
            226,
            237,
            249,
            261,
            274,
            287,
            301,
            316,
            332,
            348,
            365,
            383,
            402,
            422,
            442,
            464,
            487,
            511,
            536,
            562,
            590,
            619,
            649,
            681,
            715,
            750,
            787,
            825,
            866,
            909,
            953,
        ],
        "E96": [
            100,
            102,
            105,
            107,
            110,
            113,
            115,
            118,
            121,
            124,
            127,
            130,
            133,
            137,
            140,
            143,
            147,
            150,
            154,
            158,
            162,
            165,
            169,
            174,
            178,
            182,
            187,
            191,
            196,
            200,
            205,
            210,
            215,
            221,
            226,
            232,
            237,
            243,
            249,
            255,
            261,
            267,
            274,
            280,
            287,
            294,
            301,
            309,
            316,
            324,
            332,
            340,
            348,
            357,
            365,
            374,
            383,
            392,
            402,
            412,
            422,
            432,
            442,
            453,
            464,
            475,
            487,
            499,
            511,
            523,
            536,
            549,
            562,
            576,
            590,
            604,
            619,
            634,
            649,
            665,
            681,
            698,
            715,
            732,
            750,
            768,
            787,
            806,
            825,
            845,
            866,
            887,
            909,
            931,
            953,
            976,
        ],
    }

    def find_closest(series: List[int], target: int) -> Tuple[int, ...]:
        """
        Находит ближайшие номиналы сопротивлений в заданном ряду.

        Параметры:
        series (List[int]): Список номиналов сопротивлений.
        target (int): Значение сопротивления, для которого нужно найти ближайшие номиналы.

        Возвращает:
        Tuple[int, ...]: Кортеж с ближайшими номиналами сопротивлений.
        """
        min_diff = min(map(lambda x: abs(x - target), series))
        return tuple(filter(lambda x: abs(x - target) == min_diff, series))

    result: Dict[str, Tuple[int, ...]] = {
        series: find_closest(values, resistance)
        for series, values in resistor_series.items()
    }

    return result


# Примеры вызова функции
print(
    pick_resistors(470)
)  # что будет: {'E6': (470,), 'E12': (470,), 'E24': (470,), 'E48': (464, 487), 'E96': (464, 475)}
print(
    pick_resistors(333)
)  # Что будет {'E6': (330,), 'E12': (330,), 'E24': (330,), 'E48': (332,), 'E96': (332,)}

# Пример проверки выхода за допустимые границы
print(pick_resistors(99))  # Что вышло: None
print(pick_resistors(1000))  # что вышло: None

from typing import Generator, Tuple


def deck() -> Generator[Tuple[int, str], None, None]:
    """
    Создает упорядоченную колоду карт.

    Функция не принимает аргументы.

    Returns:
        Generator[Tuple[int, str], None, None]: Генератор, который возвращает кортежи (номинал, масть) для каждой карты.
    """
    suits = ["черви", "бубны", "пики", "трефы"]  # Список мастей карт
    ranks = range(
        2, 15
    )  # Номиналы карт от 2 до 14 (где 11 — валет, 12 — дама, 13 — король, 14 — туз)

    for suit in suits:
        for rank in ranks:
            yield (rank, suit)  # Возвращаем кортеж (номинал, масть)


# Тестирование функции вручную
if __name__ == "__main__":
    card_deck = deck()

    # Печать всех карт для проверки
    for card in card_deck:
        print(card)

"""
Ожидаемый вывод:
(2, 'черви')
(3, 'черви')
...
(14, 'черви')
(2, 'бубны')
(3, 'бубны')
...
(14, 'бубны')
(2, 'пики')
(3, 'пики')
...
(14, 'пики')
(2, 'трефы')
(3, 'трефы')
...
(14, 'трефы')
"""

from typing import Callable, List, Union


def math_function_resolver(
    math_func: Callable[[float], float],
    *args: Union[int, float],
    str_output: bool = False
) -> List[Union[int, str]]:
    """
    Функция высшего порядка для вычисления округлённых значений различных математических функций.

    :param math_func: Математическая функция, принимающая один обязательный позиционно-ключевой аргумент x.
    :param args: Произвольное количество значений x для математической функции.
    :param str_output: Переключатель типа возвращаемых значений (int или str), по умолчанию False.
    :return: Список округлённых значений математической функции для переданных значений x.
    """
    # Вычисляем значения математической функции и округляем их до целого числа
    rounded_values = [round(math_func(x)) for x in args]

    # Преобразуем значения в строку, если это требуется
    if str_output:
        return [str(value) for value in rounded_values]

    return rounded_values


# Пример использования
if __name__ == "__main__":
    import math

    # Пример использования для math.sin
    result_sin = math_function_resolver(
        math.sin, 0, math.pi / 2, math.pi, 3 * math.pi / 2, str_output=False
    )
    print(result_sin)  # Ожидаемый вывод: [0, 1, 0, -1]

    # Пример использования для math.cos
    result_cos = math_function_resolver(
        math.cos, 0, math.pi / 2, math.pi, 3 * math.pi / 2, str_output=True
    )
    print(result_cos)  # Ожидаемый вывод: ['1', '0', '-1', '0']

"""
Результаты проверки:
[0, 1, 0, -1]
['1', '0', '-1', '0']
"""

from functools import wraps
from typing import Callable


def repeat(n: int = 2) -> Callable:
    """
    Параметризуемый декоратор, который выполняет декорируемую функцию заданное количество раз.

    :param n: Количество вызовов декорируемой функции, по умолчанию 2.
    :return: Декоратор, который вызывает декорируемую функцию n раз.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# Пример использования
if __name__ == "__main__":

    @repeat(3)
    def greet(name: str) -> None:
        print(f"Hello, {name}!")

    # Ожидаемый вывод: "Hello, Vasya!" три раза
    greet("Vasya")

    @repeat()
    def add(a: int, b: int) -> int:
        result = a + b
        print(f"The result of {a} + {b} is {result}")
        return result

    # Ожидаемый вывод: "The result of 3 + 4 is 7" два раза
    add(3, 4)

import functools


def logger(func):
    @functools.wraps(
        func
    )  # Сохраняем метаданные исходной функции func для корректного отображения имени и докстринга
    def wrapper(*args, **kwargs):
        # Получение информации о переданных аргументах
        arg_names = func.__code__.co_varnames[
            : func.__code__.co_argcount
        ]  # Имена всех аргументов функции
        default_values = (
            func.__defaults__ if func.__defaults__ else ()
        )  # Значения по умолчанию для позиционных аргументов
        kw_default_values = (
            func.__kwdefaults__ if func.__kwdefaults__ else {}
        )  # Значения по умолчанию для ключевых аргументов

        # Соединение переданных значений с их именами
        arg_list = []
        for name, value in zip(arg_names, args):
            arg_list.append(f"{name}={value}")  # Добавление позиционных аргументов

        # Добавление значений по умолчанию для пропущенных аргументов
        for name, value in zip(
            arg_names[len(args) :], default_values[len(args) - len(arg_names) :]
        ):
            if name not in kwargs:
                arg_list.append(
                    f"{name}={value}"
                )  # Добавление пропущенных позиционных аргументов

        # Добавление именованных аргументов
        for key, value in kwargs.items():
            arg_list.append(f"{key}={value}")  # Добавление именованных аргументов

        # Добавление значений по умолчанию для ключевых аргументов
        for key, value in kw_default_values.items():
            if key not in kwargs:
                arg_list.append(
                    f"{key}={value}"
                )  # Добавление пропущенных ключевых аргументов

        # Формирование строки вызова функции
        arg_str = ", ".join(arg_list)  # Строка аргументов
        call_str = f"{func.__name__}({arg_str})"  # Строка вызова функции

        try:
            result = func(
                *args, **kwargs
            )  # Вызов исходной функции с переданными аргументами
            print(f"{call_str} -> {result}")  # Вывод успешного вызова с результатом
            return result
        except Exception as e:
            print(
                f"{call_str} .. {e.__class__.__name__}: {e}"
            )  # Вывод исключения в случае его возникновения
            return None  # Возвращаем None при возникновении исключения

    return wrapper


# Пример ручного теста
def div_round(num1, num2, *, digits=0):
    """Функция для деления num1 на num2 с округлением до digits знаков после запятой."""
    return round(num1 / num2, digits)


div_round = logger(div_round)  # Применяем декоратор logger к функции div_round

# Тестирование вызовов функции div_round с различными аргументами
print(div_round(1, 3, digits=2))  # Ожидается: div_round(1, 3, digits=2) -> 0.33
print(div_round(7, 2))  # Ожидается: div_round(7, 2, digits=0) -> 4.0
print(
    div_round(5, 0)
)  # Ожидается: div_round(5, 0, digits=0) .. ZeroDivisionError: division by zero

# Описание декоратора
"""
Описание декоратора 

1. Получаем метаданные исходной функции, чтобы сохранить её имя и другие атрибуты при обертывании.
2. Формируем список аргументов, включая переданные и значения по умолчанию.
3. Формируем строку вызова функции для отображения в журнале.
4. Выполняем вызов функции с переданными аргументами и ловим исключения при их возникновении.
5. Выводим в стандартный вывод результат вызова или информацию об исключении.


