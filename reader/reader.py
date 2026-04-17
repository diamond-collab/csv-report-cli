import csv


def read_csv_files(
    files: list[str],
) -> list[dict[str, str]]:
    """
    Читает CSV-файлы и возвращает их содержимое.
    Объединяет строки из всех переданных файлов в один список словарей.

    :param files: список путей к CSV-файлам.
    :return: список словарей, где каждая строка файла представлена как dict
    :raises FileNotFoundError: если указанный файл не найден
    """
    all_rows = []
    for file in files:
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                all_rows.append(row)

    return all_rows
