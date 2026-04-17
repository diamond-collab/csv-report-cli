import argparse

from reader import read_csv_files
from report import build_report
from output import render_report_table

parser = argparse.ArgumentParser()

parser.add_argument('--files', nargs='+')
parser.add_argument('--report')

args = parser.parse_args()


def main() -> None:
    """
    Основная функция приложения.

    Читает CSV-файлы, строит отчет по выбранному типу и выводит результат в консоль.

    Обрабатывает ошибки:
    - ValueError - если указан неихвестный отчет
    - FileNotFoundError - если файл не найден
    """
    try:
        all_rows = read_csv_files(args.files)
        result_rows = build_report(report=args.report, all_rows=all_rows)
        render_report_table(result_rows)
    except ValueError as v_error:
        print(v_error)
    except FileNotFoundError:
        label = 'Файлы' if len(args.files) > 1 else 'Файл'
        msg = 'не найдены' if len(args.files) > 1 else 'не найден'
        text = ', '.join(args.files)
        print(f'{label} {text} {msg}')


if __name__ == '__main__':
    main()
