import uuid
import json
import time
from typing import Dict, Any


def get_input(prompt: str, validator: callable, error_message: str) -> Any:
    """Получает ввод от пользователя и проверяет его с помощью функции-валидатора."""
    while True:
        user_input = input(prompt)
        try:
            validated_input = validator(user_input)
            return validated_input
        except ValueError:
            print(error_message)


def validate_rank(rank: str) -> int:
    """Проверяет, что ранг - это целое число от 1 до 22."""
    rank_int = int(rank)
    if 1 <= rank_int <= 22:
        return rank_int
    raise ValueError()


def validate_car(car: str) -> str:
    """Проверяет, что номер машины - это целое число от 1 до 30 и форматирует его."""
    car_int = int(car)
    if 1 <= car_int <= 30:
        return f"{car_int:02d}"
    raise ValueError()


def generate_filename() -> str:
    """Генерирует уникальное имя файла."""
    timestamp = int(time.time())
    random_id = uuid.uuid4().hex[:8]
    return f"data_{timestamp}_{random_id}.json"


def save_data(data: Dict[str, Any], filename: str) -> None:
    """Сохраняет данные в JSON файл."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    name = input("Введите Ваше имя и фамилию: ")
    rank = get_input(
        "Введите порядковый ранг: ",
        validate_rank,
        "Некорректный ввод. Введите число от 1 до 22."
    )
    car = get_input(
        "Введите порядковый номер т/с: ",
        validate_car,
        "Некорректный ввод. Введите число от 1 до 30."
    )

    hush_id = str(uuid.uuid4())
    filename = generate_filename()

    data = {
        "name": name,
        "rank": rank,
        "car": car,
        "hush_id": hush_id
    }

    save_data(data, filename)

    print(f"Автор: {name} | {rank}")
    print(f"Номер т/с: {car}")
    print(f"Hush-id: {hush_id}")
    print(f"Данные сохранены в файл {filename}")


if __name__ == "__main__":
    main()