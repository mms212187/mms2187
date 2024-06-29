import random

random_list = [random.randint(-100, 100) for _ in range(20)]

min_element = min(random_list)
max_element = max(random_list)

negative_count = sum(1 for x in random_list if x < 0)
positive_count = sum(1 for x in random_list if x > 0)
zero_count = sum(1 for x in random_list if x == 0)

print(f"Список: {random_list}")
print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
print(f"Количество отрицательных элементов: {negative_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zero_count}")


def remove_duplicates(lst):
    return list(set(lst))


initial_list = [10, 20, 10, 20, 30, 40, 30, 50]
result_list = remove_duplicates(initial_list)
print("Начальный список:", initial_list)
print("Список без дубликатов:", result_list)
