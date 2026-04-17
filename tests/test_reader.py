import pytest

from reader import read_csv_files


@pytest.mark.parametrize(
    'files',
    [
        ['test_stats1.csv'],
        ['test_stats1.csv', 'stats2.csv'],
    ],
)
def test_read_csv_files_returns_rows(
    files,
):
    rows = read_csv_files(files)

    assert isinstance(rows, list)
    assert len(rows) > 0
    assert isinstance(rows[0], dict)

    assert 'title' in rows[0]
    assert 'ctr' in rows[0]
    assert 'retention_rate' in rows[0]


@pytest.mark.parametrize(
    'unknown_files',
    [
        ['unknown_file.csv'],
        ['missing.csv'],
    ],
)
def test_read_csv_files_raises_for_missing_file(
    unknown_files,
):
    with pytest.raises(FileNotFoundError):
        read_csv_files(unknown_files)
