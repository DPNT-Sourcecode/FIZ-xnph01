# noinspection PyUnusedLocal
def fizz_buzz(number):
    strings = []
    numstring = str(number)
    # fizz if divisible by 3 or has a 3 in it
    if (number % 3 == 0) or ("3" in numstring):
        strings.append("fizz")
    # buzz if divisible by 5 or it has a 5 in it:
    if (number % 5 == 0) or ("5" in numstring):
        strings.append("buzz")
    """
    Deluxe if div by 3 and contains a 3
    or div by 5 and contains a 5
    still fake deluxe if odd
    """
    if (
        (
            (number % 3 == 0) and ("3" in numstring)
        ) or
        (
            (number % 5 == 0) and ("5" in numstring)
        )
    ):
        if number % 2 == 0:
            strings.append("deluxe")
        else:
            strings.append("fake deluxe")
    if len(strings) > 0:
        return(" ".join(strings))
    else:
        return(numstring)

