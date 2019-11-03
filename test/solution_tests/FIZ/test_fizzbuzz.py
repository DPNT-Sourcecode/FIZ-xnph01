from solutions.FIZ import fizz_buzz_solution


class TestSum():
    def test_fizz_div_by_3(self):
        assert fizz_buzz_solution.fizz_buzz(6) == "fizz"
    def test_fizz_includes_3(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"
    def test_buzz_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(10) == "buzz"
    def test_buzz_include_5(self):
        assert fizz_buzz_solution.fizz_buzz(502) == "buzz"
    def test_fizz_buzz_div_by_3_and_5(self):
        assert fizz_buzz_solution.fizz_buzz(60) == "fizz buzz"
    def test_fizz_buzz_div_by_3_contains_5(self):
        assert fizz_buzz_solution.fizz_buzz(501) == "fizz buzz"
    def test_fizz_buzz_contains_3_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(6310) == "fizz buzz"
    def test_fizz_buzz_contains_3_and_5(self):
        assert fizz_buzz_solution.fizz_buzz(503) == "fizz buzz"
    def test_deluxe_contains_3_and_div_by_3(self):
        assert fizz_buzz_solution.fizz_buzz(36) == "fizz deluxe"
    def test_deluxe_contains_5_and_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(50) == "buzz deluxe"
    def test_fake_deluxe_contains_3_and_div_by_3(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz fake deluxe"
    def test_fake_deluxe_contains_5_and_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz fake deluxe"
    def test_neither(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"

