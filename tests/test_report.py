import pytest

from reader import read_csv_files
from report import build_report


@pytest.mark.parametrize(
    'files, report_name',
    [
        (['test_stats1.csv'], 'clickbait'),
        (['test_stats1.csv', 'stats2.csv'], 'clickbait'),
    ],
)
def test_build_report_filters_and_sorts_clickbait_rows(files, report_name):
    rows = read_csv_files(files)

    report_rows = build_report(report_name, rows)
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


@pytest.mark.parametrize(
    'files, unknown_report',
    [
        (['test_stats1.csv'], 'cli'),
        (['test_stats1.csv'], 'unknown'),
        (['test_stats1.csv'], 'fake_report'),
    ],
)
def test_build_report_raises_for_unknown_report(files, unknown_report):
    all_rows = read_csv_files(files)

    with pytest.raises(ValueError, match=f'Неизвестный тип отчета {unknown_report}'):
        build_report(unknown_report, all_rows)
