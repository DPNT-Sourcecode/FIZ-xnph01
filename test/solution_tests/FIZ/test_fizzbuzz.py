from solutions.FIZ import fizz_buzz_solution


class TestSum():
    def test_fizz(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"
    def test_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"
    def test_fizz_buzz(self):
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"
    def test_neither(self):
        assert fizz_buzz_solution.fizz_buzz(7) == 7
