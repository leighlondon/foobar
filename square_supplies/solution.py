"""
The solution to the "square_supplies" problem.
"""
import math


def answer(n):
    """
    Finding the smallest number of squares that need to be summed to
    create n.
    """
    # Generate a list of the square numbers less than n in descending order.
    # It uses a comprehension to create a list of squares less than n by
    # iterating from sqrt(n) down and generating the square of that number,
    # which means that you don't need to check if it's an integer and don't
    # waste cycles on the numbers that aren't needed.
    squares = [x*x for x in xrange(int(math.sqrt(n)), 0, -1)]

    # First check if it's just a square.
    if n in squares:
        return 1

    # If it's twice a square, that's going to be smallest.
    # Divide by a float to stop integer division truncation problems.
    if n / 2.0 in squares:
        return 2

    # If it gets to here, run the "brute force" method.
    return solve(n, squares)


def next_square(n, squares):
    """
    A helper function to tell me the next square.
    Mostly to keep the code tidy and easier to follow.
    """
    # Start at the front of the list.
    i = 0
    while i < len(squares):
        # Once n is greater than or equal, return that square.
        if n >= squares[i]:
            return squares[i]
        # Otherwise, keep going.
        i = i + 1


def solve(n, squares):
    """
    A brute force algorithm.

    Needs to have a list of squares less than n.
    """
    # Take the smallest biggest square less than n from it, and iterate lower
    # until the number is 0. Repeat this again from the second biggest down,
    # and return the lowest number of "steps".
    counters = []

    # Loop through the list of squares until the mid-point. The optimal
    # solution is usually found within the first few, however.
    # There are a few edge cases that need to go deeper though-
    # the perfect example being 12, which has an optimal solution of 3,
    # or 12 = 4 + 4 + 4. The regular algorithm approach will stop with
    # 12 = 9 + 1 + 1 + 1 => 4 though, so going past the mid-point of the
    # list of squares resolves this.
    for i in range(0, len(squares)/2 + 1):

        # Set the initial value based on the index.
        current = n - squares[i]
        count = 1

        # While there's still a number, keep subtracting the next highest
        # squared value using the squares list as a reference.
        # Increase the count of squares that have been subtracted.
        while current > 0:
            current = current - next_square(current, squares)
            count = count + 1

        # Append the result to the total list once it's calculated.
        counters.append(count)

    # Return the smallest value (sort and return the first item).
    return sorted(counters)[0]
