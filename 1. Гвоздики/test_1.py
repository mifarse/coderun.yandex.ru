import io
from main import main
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("6\n3 13 12 4 14 6\n", "5\n"),
    ],
)
def test_1(capsys, monkeypatch, test_input, expected):
    """Проверяет решение."""
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
