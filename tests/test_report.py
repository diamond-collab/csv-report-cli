import pytest

from reader import read_csv_files
from report import build_report

files = ['test_stats1.csv']
report_name = 'clickbait'
unknown_report = 'cli'


def test_build_report_filters_and_sorts_clickbait_rows():
    all_rows = read_csv_files(files)
    assert len(all_rows) > 0

    report_rows = build_report(report_name, all_rows)
    assert isinstance(report_rows, list)
    assert len(report_rows) > 0
    assert isinstance(report_rows[0], dict)

    assert 'title' in report_rows[0]
    assert 'ctr' in report_rows[0]
    assert 'retention_rate' in report_rows[0]

    for row in report_rows:
        assert row['ctr'] > 15
        assert row['retention_rate'] < 40

    for idx in range(len(report_rows) - 1):
        assert report_rows[idx]['ctr'] >= report_rows[idx + 1]['ctr']


def test_build_report_raises_for_unknown_report():
    all_rows = read_csv_files(files)
    assert len(all_rows) > 0

    with pytest.raises(ValueError, match=f'Неизвестный тип отчета {unknown_report}'):
        build_report(unknown_report, all_rows)
