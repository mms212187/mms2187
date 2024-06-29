def find_common_elements(tuple1, tuple2, tuple3):
    common_elements = list(filter(lambda x: x in tuple2 and x in tuple3, tuple1))
    return common_elements


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

common_elements = find_common_elements(tuple1, tuple2, tuple3)
print(common_elements)


def find_unique_elements(tuple1, tuple2, tuple3):
    unique_in_tuple1 = [x for x in tuple1 if x not in tuple2 and x not in tuple3]
    unique_in_tuple2 = [x for x in tuple2 if x not in tuple1 and x not in tuple3]
    unique_in_tuple3 = [x for x in tuple3 if x not in tuple1 and x not in tuple2]
    return unique_in_tuple1 + unique_in_tuple2 + unique_in_tuple3


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

unique_elements = find_unique_elements(tuple1, tuple2, tuple3)
print(unique_elements)


def print_info(name, **kwargs):
    print(f"Имя: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


print_info("Алексей", возраст=25, профессия="дизайнер", город="Санкт-Петербург")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mapped_result = list(map(lambda x: x**2 if x % 2 != 0 else x**3, numbers))
print(mapped_result)
