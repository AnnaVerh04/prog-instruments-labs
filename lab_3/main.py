import csv
import re
from checksum import calculate_checksum, serialize_result

PATTERNS = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "shils": r"^[0-9]{11}$",
    "identifier": r"^[0-9]{2}\-[0-9]{2}\/[0-9]{2}$",
    "ip_v4": r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|"
             r"[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    "longitude": r"^-?((1[0-7]\d|\d?\d)(?:\.\d{1,})?|180(\.0{1,})?)$",
    "blood_type": r"^(?:AB|A|B|O)[+\u2212]$",
    "isbn": r"^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": r"^[a-z]{1,3}(-[a-z]+)?(-[a-z]{2})?$",
    "date": r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-9]|3[0-1])$"
}


def read_csv(file_name) -> list:
    """
    Метод для чтения данных из CSV файла.

    :param file_name: имя файла, который необходимо прочитать.
    :return: список строк, считанных из файла, без заголовка.
    """
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
        return data


def is_row_valid(row: list) -> bool:
    """
    Метод для проверки валидности строки данных.

    :param row: список значений, представляющих строку данных.
    :return: True, если строка валидна, иначе False.
    """
    for key, value in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[key], value, re.X):
            return False
    return True


def find_invalid_rows(data: list) -> list:
    """
    Метод для поиска индексов невалидных строк в данных.

    :param data: список строк данных для проверки.
    :return: список индексов невалидных строк.
    """
    invalid_indices = []
    for i, row in enumerate(data):
        if not is_row_valid(row):
            invalid_indices.append(i)
    return invalid_indices


if __name__ == "__main__":
    data = read_csv("66.csv")
    invalid_numbers = find_invalid_rows(data)
    serialize_result(66, calculate_checksum(list(invalid_numbers)))
