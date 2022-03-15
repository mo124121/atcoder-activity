def addition(*args):
    a1, a2 = args
    return a1 + a2


def multiply(num1, num2):
    total = 0
    for _ in range(num2):
        total = addition(total, num1)
    return total


class TestAddtion:
    def test_main(self):
        result = addition(3, 2)
        assert result == 5

    def test_treeargs(self):
        result = addition(3, 2, 1)
        assert result == 6

    def test_noargs(self):
        result = addition()
        assert result == 0
