from typing import Any

from tabulate import tabulate


def render_report_table(
    rows: list[dict[str, Any]],
) -> None:
    """
    Формирует и выводит таблицу в консоль.

    Создает таблицу из списка словарей и отображает ее с помощью библиотеки tabulate.
    :param rows: список словарей с данными отчета
    :return: None
    """
    table = tabulate(
        rows,
        headers='keys',
        tablefmt='grid',
    )
    print(table)
