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
    # deluxe if greater than 10 and all the digits are identical
    # fake deluxe if also odd
    # again presumably e.g. fizz fake deluxe
    if (number > 10) and (numstring == len(numstring) * numstring[0]):
        if number % 2 == 0:
            strings.append("deluxe")
        else:
            strings.append("fake deluxe")
    if len(strings) > 0:
        return(" ".join(strings))
    else:
        return(numstring)
