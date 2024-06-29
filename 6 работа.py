import re

text = """
Сегодня на выезды потребуется отправить трёх-четырёх специалистов, остальных держите в офисе. Некоторые заявки пришли на конкретных людей, но можно вызвать и других, смотрите по ситуации, как лучше их отправить, чтобы всех объездить сегодня.
Петрову П. П. попросили выехать по адресам ул. Культуры 78 кв. 6, улица Мира дом 12Б квартира 144. Смирнова С. С. просят подъехать только по адресу: Восьмого Марта 106-19. Без предпочтений по специалистам пришли запросы с адресов: улица Свободы 54 6, Улица Шишкина дом 9 кв. 15, ул. Лермонтова 18 кв. 93.
"""

addresses = re.findall(
    r"(?:ул\.|улица)\s*([^\s,]+)\s*(?:дом|кв\.|квартира)?\s*([^\s,]+)?\s*(?:кв\.|квартира)?\s*(\d+)",
    text,
)
formatted_addresses = [
    "{} {}-{}".format(address[0], address[1] if address[1] else "", address[2])
    for address in addresses
]

for formatted_address in formatted_addresses:
    print(formatted_address)

special_address = re.search(r"Восьмого\s+Марта\s+(\d+-\d+)", text)
if special_address:
    print(special_address.group(0))

shishkina_address = re.search(r"Шишкина\s+дом\s+(\d+)\s+кв\.\s+(\d+)", text)
if shishkina_address:
    print(
        "Шишкина {}-{}".format(shishkina_address.group(1), shishkina_address.group(2))
    )

mira_address = re.search(r"Мира\s+(\d+[А-Я])\s+кв\.\s+(\d+)", text)
if mira_address:
    print("Мира {}-{}".format(mira_address.group(1), mira_address.group(2)))
