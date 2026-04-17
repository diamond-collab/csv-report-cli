import pytest

from reader import read_csv_files

files = ['test_stats1.csv']
unknown_file = ['unknown_file.csv']


def test_read_csv_files_returns_rows():
    rows = read_csv_files(files)

    assert isinstance(rows, list)
    assert len(rows) > 0
    assert isinstance(rows[0], dict)
    assert 'title' in rows[0]
    assert 'ctr' in rows[0]
    assert 'retention_rate' in rows[0]
    assert rows[0]['title'] == 'Я бросил IT и стал фермером'


def test_read_csv_files_raises_for_missing_file():
    with pytest.raises(FileNotFoundError):
        read_csv_files(unknown_file)
