from calculator import divide


def test_normal_division():
    assert divide(10, 2) == 5


def test_decimal_division():
    assert divide(5, 2) == 2.5