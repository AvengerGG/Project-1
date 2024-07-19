import uuid
import json
import time

name = input("Введите Ваше имя и фамилию: ")
while True:
    rank = input("Введите порядковый ранг: ")
    try:
        rank = int(rank)
        if 1 <= rank <= 22:
            break
        else:
            print("Номер должен быть в диапазоне от 1 до 22.")
    except ValueError:
        print("Некорректный ввод. Введите число.")

while True:
    car_input = input("Введите порядовый номер т/с: ")
    try:
        car = int(car_input)
        if 1 <= car <= 30:
            break
        else:
            print("Номер должен быть в диапазоне от 01 до 30.")
    except ValueError:
        print("Некорректный ввод. Введите число.")

timestamp = int(time.time())
car = car
file_name = f"data_{timestamp}_{car}.json"

data = {
    "name": name,
    "rank": rank,
    "car": car_input,
    "hush_id": str(uuid.uuid4())
}

with open(file_name, "w") as f:  # Используем file_name для сохранения
    json.dump(data, f)

print("Автор:", name, "|", rank)
print("Номер т/с:", car_input)
print("Hush-id:", uuid.uuid4())
print(f"Данные сохранены в файл {file_name}")