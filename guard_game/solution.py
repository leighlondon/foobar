def answer(x):
    # adding the digits recursively to a number.

    # set the value for the initial round.
    num = x

    # keep going while there's more than one digit.
    while len(str(num)) > 1:

        # initialise the round sum to be 0.
        s = 0

        # sum all of the digits of the current number (num).
        for i in range(0, len(str(num))):
            s = s + int(str(num)[i])

        # set this as the new number.
        num = s

    # return the result.
    return num
