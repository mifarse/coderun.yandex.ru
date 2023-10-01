import io
from main import main
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1\n1\n1\n1\n1", "YES\n"),
        ("2\n2\n2\n1\n1", "NO\n"),
    ],
)
def test_1(capsys, monkeypatch, test_input, expected):
    """Проверяет решение."""
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
