from solutions.FIZ import fizz_buzz_solution


class TestSum():
    def test_fizz_div_by_3(self):
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"
    def test_fizz_includes_3(self):
        assert fizz_buzz_solution.fizz_buzz(13) == "fizz"
    def test_buzz_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"
    def test_buzz_include_5(self):
        assert fizz_buzz_solution.fizz_buzz(502) == "buzz"
    def test_fizz_buzz_div_by_3_and_5(self):
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"
    def test_fizz_buzz_div_by_3_contains_5(self):
        assert fizz_buzz_solution.fizz_buzz(501) == "fizz buzz"
    def test_fizz_buzz_contains_3_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(35) == "fizz buzz"
    def test_fizz_buzz_contains_3_and_5(self):
        assert fizz_buzz_solution.fizz_buzz(503) == "fizz buzz"
    def test_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(11) == "deluxe"
    def text_deluxe_div_by_3(self):
        assert fizz_buzz_solution.fizz_buzz(66) == "fizz deluxe"
    def text_deluxe_contains_3(self):
        # think this is redundant as also div by 3 in all cases
        assert fizz_buzz_solution.fizz_buzz(33) == "fizz deluxe"
    def text_deluxe_div_by_5(self):
        assert fizz_buzz_solution.fizz_buzz(55) == "fizz deluxe"
    def text_fizz_buzz_deluxe(self):
        assert fizz_buzz_solution.fizz_buzz(555) == "fizz buzz deluxe"
    def test_neither(self):
        assert fizz_buzz_solution.fizz_buzz(7) == "7"
