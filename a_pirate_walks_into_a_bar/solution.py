def answers(numbers):

    # Create an empty list, to put the pirates as they're met.
    pirates = []
    # Start at pirate 0.
    i = 0

    # Keep going until the cycle is found.
    while True:

        # Check the current pirate matches any existing pirates.
        # As they're added sequentially, any previous pirate means that
        # there's now a cycle. The length of the cycle is the length of
        # the list, minus the index of the pirate that was just found.
        if i in pirates:
            return len(pirates) - pirates.index(i)

        # Otherwise, append the current pirate.
        pirates.append(i)

        # Move to the next pirate.
        i = numbers[i]
