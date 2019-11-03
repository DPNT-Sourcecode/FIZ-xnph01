# noinspection PyUnusedLocal
def fizz_buzz(number):
    strings = []
    # fizz if divisible by 3 or has a 3 in it
    if (number % 3 == 0) or ("3" in str(number)):
        strings.append("fizz")
    # buzz if divisible by 5 or it has a 5 in it:
    if (number % 5 == 0) or ("5" in str(number)):
        strings.append("buzz")
    if len(strings) > 0:
        return(" ".join(strings))
    else:
        return(str(number))

