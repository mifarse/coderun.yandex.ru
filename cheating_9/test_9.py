import io
import pytest
from .main import main


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            """3 2
            1 2
            2 3
            """, "YES\n"
        ),
        (
            """3 3
            1 2
            2 3
            1 3
            """, "NO\n")
    ],
)
def test_1(capsys, monkeypatch, test_input, expected):
    """Проверяет решение."""
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
