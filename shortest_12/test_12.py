import io
import textwrap
from .main import main
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            textwrap.dedent(
                """10
                0 1 0 0 0 0 0 0 0 0
                1 0 0 1 1 0 1 0 0 0
                0 0 0 0 1 0 0 0 1 0
                0 1 0 0 0 0 1 0 0 0
                0 1 1 0 0 0 0 0 0 1
                0 0 0 0 0 0 1 0 0 1
                0 1 0 1 0 1 0 0 0 0
                0 0 0 0 0 0 0 0 1 0
                0 0 1 0 0 0 0 1 0 0
                0 0 0 0 1 1 0 0 0 0
                5 4
                """
            ), "2\n"),
        (
            textwrap.dedent(
                """5
                0 1 0 0 1
                1 0 1 0 0
                0 1 0 0 0
                0 0 0 0 0
                1 0 0 0 0
                3 5
                """
            ), "3\n"),
    ],
    ids=["yandex 10x10", "yandex 5x5"]
)
def test_1(capsys, monkeypatch, test_input, expected):
    """Проверяет решение."""
    monkeypatch.setattr("sys.stdin", io.StringIO(test_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
