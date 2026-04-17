from typing import Any


def build_report(
    report: str,
    all_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """
    Строит отчет по указанному типу.
    Выбирает соответствующую функцию обработки и возвращает
    результат отчета на основе переданных данных.

    :param report: название отчета (например 'clickbait')
    :param all_rows: список словарей с данными из CSV-файлов
    :return: список словарей с результатами отчета
    :raises ValueError: если указан неизвестный тип отчета: {report}
    """
    # Словарь доступных отчетов.
    # Чтобы добавить новый отчет, достаточно указать: имя отчета -> функция генерации
    report_handlers = {
        'clickbait': generate_clickbait_report,
    }

    report_function = report_handlers.get(report)
    if report_function is None:
        raise ValueError(f'Неизвестный тип отчета {report}')

    return report_function(all_rows=all_rows)


def generate_clickbait_report(
    all_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """
    Формирует отчет clickbait.

    Отбирает видео с CTR > 15 и retention_rate < 40,
    оставляет только нужные поля и сортирует результат по убываюнию CTR.

    :param all_rows: список словарей с данными из CSV-файлов
    :return: список словарей с полями title, ctr и retention_rate
    """
    rows = []
    for row in all_rows:
        if float(row['ctr']) > 15 and float(row['retention_rate']) < 40:
            result_row = {
                'title': row['title'],
                'ctr': float(row['ctr']),
                'retention_rate': float(row['retention_rate']),
            }
            rows.append(result_row)

    filtered_rows = sorted(rows, key=lambda r: r['ctr'], reverse=True)

    return filtered_rows
