import io
from main import main
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("5\n35\n40\n101\n59\n63\n", "235\n0 1\n5\n"),
        ("5\n110\n40\n120\n110\n60\n", "260\n0 2\n3\n5\n"),
        ("3\n110\n110\n110\n", "220\n1 1\n2\n"),
    ],
)
def test_5(capsys, monkeypatch, test_input, expected):
    """Проверяет решение. Инпут найден на просторах интернета."""
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
