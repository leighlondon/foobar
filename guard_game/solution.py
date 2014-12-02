def answer(x):
    """
    Adding the digits of a number recursively.
    """
    # Set the value for the initial round.
    number = x
    # Keep going while there's more than one digit.
    while len(str(number)) > 1:
        # Initialise the round sum to be 0.
        round_sum = 0
        # Sum all of the digits of the current number.
        for i in range(0, len(str(number))):
            round_sum = round_sum + int(str(number)[i])
        # Set this round sum as the new number.
        number = round_sum
    # Return the result.
    return number
