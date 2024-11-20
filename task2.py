import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Считываем содержание файла csv
    with open(INPUT_FILENAME, encoding='utf-8') as file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(file, delimiter=",")

        # Получаем заголовки из первой строки
        headers = next(file_reader)
        print(f'Файл содержит столбцы: {", ".join(headers)}')

        # Список для хранения данных
        data = []

        # Считывание данных из CSV файла
        for row in file_reader:
            # Создаем словарь, используя заголовки как ключи
            data.append({headers[i]: row[i] for i in range(len(headers))})

        print(f'Всего в файле {len(data) + 1} строк.')  # +1 для заголовков

    # Сериализация данных в JSON файл с отступами 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
        json.dump(data, output_f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    task()

    # Чтение и вывод содержимого JSON файла
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
