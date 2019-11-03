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
    # WHAT HAPPENS IF SOMETHING IS EITHER FIZZ & DELUXE (BUT NOT BUZZ)
    # OR BUZZ AND DELUXE (BUT NOT FIZZ)?
    # I am assuming "fizz deluxe" or "buzz deluxe"
    if (number > 10) and (numstring == len(numstring) * numstring[0]):
        strings.append("deluxe")
    if len(strings) > 0:
        return(" ".join(strings))
    else:
        return(numstring)

