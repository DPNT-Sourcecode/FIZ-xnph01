# noinspection PyUnusedLocal
def fizz_buzz(number):
    strings = []
    if number % 3 == 0:
        strings.append("fizz")
    if number % 5 == 0:
        strings.append("buzz")
    if len(strings) > 0:
        return(" ".join(strings))
    else:
        return(number)
